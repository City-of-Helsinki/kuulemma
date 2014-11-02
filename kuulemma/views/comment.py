from flask import Blueprint, jsonify, request

from kuulemma.extensions import db
from kuulemma.models import Comment, Hearing
from kuulemma.schemas import CommentSchema

comment = Blueprint(
    name='comment',
    import_name=__name__,
    url_prefix='/hearings/<int:hearing_id>/links/comments'
)


@comment.route('')
def index(hearing_id):
    comments = Comment.query.filter(Comment.hearing_id == hearing_id).all()
    serialized = CommentSchema(comments, many=True)
    return jsonify({'comments': serialized.data}), 200


@comment.route('', methods=['POST'])
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
