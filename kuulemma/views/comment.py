from flask import abort, Blueprint, jsonify, request
from flask.ext.login import current_user
from sqlalchemy.orm.exc import NoResultFound

from kuulemma.extensions import db
from kuulemma.models import Comment, Hearing, Like, User
from kuulemma.schemas import CommentSchema

comment = Blueprint(
    name='comment',
    import_name=__name__,
    url_prefix=''
)


@comment.route('/kuulemiset/<int:hearing_id>/links/comments')
def index(hearing_id):
    comments = Comment.query.filter(Comment.hearing_id == hearing_id).all()
    serialized = CommentSchema(comments, many=True)
    return jsonify({'comments': serialized.data}), 200


@comment.route('/kuulemiset/<int:hearing_id>/links/comments', methods=['POST'])
def create(hearing_id):
    hearing = Hearing.query.get_or_404(hearing_id)

    schema = CommentSchema()
    data = schema.load(request.get_json())

    if data.errors:
        return jsonify({'error': data.errors}), 400

    data = data.data
    comment = Comment(
        hearing=hearing,
        title=data['title'],
        body=data['body'],
        username=data['username']
    )

    db.session.add(comment)
    db.session.commit()

    return jsonify({'comments': CommentSchema(comment).data}), 201


@comment.route('/comments/<int:comment_id>/links/likes', methods=['POST'])
def like(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    user_id = request.get_json().get('user_id', 0)
    user = User.query.get_or_404(user_id)

    if user != current_user:
        abort(401)

    try:
        like = (
            Like.query
            .filter(User.id == user_id, Comment.id == comment_id)
            .one()
        )
        db.session.delete(like)
    except NoResultFound:
        like = Like(
            user=user,
            comment=comment
        )
        db.session.add(like)

    db.session.commit()

    return jsonify({'like_count': comment.like_count}), 201
