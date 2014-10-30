from flask import Blueprint, jsonify

from kuulemma.models import Comment
from kuulemma.schemas import CommentSchema

comment = Blueprint(
    name='comment',
    import_name=__name__,
    url_prefix='/kuulemiset/<int:hearing_id>/links/comments'
)


@comment.route('')
def index(hearing_id):
    comments = Comment.query.filter(Comment.hearing_id == hearing_id).all()
    serialized = CommentSchema(comments, many=True)
    return jsonify({'comments': serialized.data}), 200
