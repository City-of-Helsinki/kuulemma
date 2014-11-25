from flask import Blueprint, jsonify, request

from kuulemma.extensions import db
from kuulemma.models import Feedback

feedback = Blueprint(
    name='feedback',
    import_name=__name__,
    url_prefix='/feedback'
)


@feedback.route('', methods=['POST'])
def create():
    if not request.get_json():
        return jsonify({'error': 'Data should be in json format'}), 400

    content = request.get_json().get('content', '')

    if not content:
        return jsonify({'error': 'There was no content'}), 400

    feedback = Feedback(content=content)
    db.session.add(feedback)
    db.session.commit()

    return jsonify({
        'feedback': {
            'id': feedback.id,
            'content': feedback.content
        }
    }), 201
