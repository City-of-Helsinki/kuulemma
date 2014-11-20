from datetime import datetime

from flask import abort, Blueprint, jsonify, request
from flask.ext.login import current_user

from kuulemma.extensions import db
from kuulemma.models import Comment, Hearing
from kuulemma.models.comment import COMMENTABLE_TYPES
from kuulemma.schemas import CommentSchema

comment = Blueprint(
    name='comment',
    import_name=__name__,
    url_prefix='/hearings/<int:hearing_id>/links/comments'
)


@comment.route('')
def index(hearing_id):
    hearing = Hearing.query.get_or_404(hearing_id)
    comments = (
        hearing
        .all_comments
        .options(db.joinedload(Comment.comment))
        .options(db.joinedload(Comment.image))
        .options(db.joinedload(Comment.alternative))
        .order_by(Comment.created_at)
    )

    if not (
        current_user.is_authenticated() and
        (current_user.is_official or current_user.is_admin)
    ):
        comments = comments.filter_by(is_hidden=False)

    serialized = CommentSchema(
        comments,
        exclude=('object_type', 'object_id'),
        many=True
    )
    return jsonify({'comments': serialized.data}), 200


@comment.route('', methods=['POST'])
def create(hearing_id):
    Hearing.query.get_or_404(hearing_id)

    schema = CommentSchema()
    data, errors = schema.load(request.get_json())

    if errors:
        return jsonify({'error': errors}), 400

    commented_object = (
        COMMENTABLE_TYPES[data['object_type']].query
        .get(int(data['object_id']))
    )

    if not commented_object:
        return jsonify(
            {'error': 'The target of this comment was not found.'}
        ), 400

    # TODO: Check that the commented object belongs to the hearing.

    comment = Comment(
        title=data['title'],
        body=data['body'],
        username=data['username']
    )
    setattr(comment, data['object_type'], commented_object)

    db.session.add(comment)
    db.session.commit()

    return jsonify({'comments': CommentSchema(comment).data}), 201


@comment.route('/<int:comment_id>', methods=['PUT'])
def update(hearing_id, comment_id):
    if not (
        current_user.is_authenticated() and
        (current_user.is_official or current_user.is_admin)
    ):
        abort(401)

    Hearing.query.get_or_404(hearing_id)
    comment = Comment.query.get_or_404(comment_id)

    if not request.get_json():
        abort(400)

    schema = CommentSchema(
        only=('title', 'body', 'username', 'is_hidden')
    )
    data, errors = schema.load(request.get_json())

    if errors:
        return jsonify({'error': errors}), 400

    comment.title = data['title']
    comment.body = data['body']
    comment.username = data['username']
    comment.is_hidden = data['is_hidden']
    comment.updated_at = datetime.utcnow()
    db.session.commit()

    serialized = CommentSchema(
        comment,
        exclude=('object_type', 'object_id')
    )

    return jsonify({'comment': serialized.data}), 200
