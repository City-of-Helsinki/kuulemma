from flask import abort, Blueprint, jsonify, request
from flask.ext.login import current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from kuulemma.extensions import db
from kuulemma.models import Comment, Like, User

like = Blueprint(
    name='like',
    import_name=__name__,
    url_prefix='/users/<int:user_id>/links/likes'
)


@like.route('', methods=['POST'])
def create(user_id):
    user = User.query.get_or_404(user_id)
    if user != current_user:
        abort(401)

    comment_id = request.get_json().get('comment_id', 0)
    comment = Comment.query.get_or_404(comment_id)

    like = Like(
        user=user,
        comment=comment
    )
    db.session.add(like)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return (
            jsonify({'error': 'User has already liked the comment.'}),
            400
        )

    return jsonify({'like_count': comment.like_count}), 201


@like.route('', methods=['DELETE'])
def delete(user_id):
    user = User.query.get_or_404(user_id)
    if user != current_user:
        abort(401)

    comment_id = request.get_json().get('comment_id', 0)

    try:
        like = (
            Like.query
            .filter(User.id == user_id, Comment.id == comment_id)
            .one()
        )
        db.session.delete(like)
    except NoResultFound:
        return (
            jsonify({'error': 'No comment was found.'}),
            400
        )

    db.session.commit()
    return '', 204
