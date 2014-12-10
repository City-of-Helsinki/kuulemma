# -*- coding: utf-8 -*-
# Kuulemma
# Copyright (C) 2014, Fast Monkeys Oy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flask import abort, Blueprint, jsonify, request
from flask.ext.mail import Message

from kuulemma.extensions import db, mail
from kuulemma.models import Feedback
from kuulemma.settings.base import FEEDBACK_RECIPIENTS

feedback = Blueprint(
    name='feedback',
    import_name=__name__,
    url_prefix='/feedback'
)


@feedback.route('', methods=['POST'])
def create():
    if not request.get_json():
        return jsonify({'error': 'Data should be in json format'}), 400

    if is_spam(request.get_json()):
        abort(400)

    content = request.get_json().get('content', '')
    if not content:
        return jsonify({'error': 'There was no content'}), 400
    feedback = Feedback(content=content)
    db.session.add(feedback)
    db.session.commit()

    message = Message(
        sender='noreply@hel.fi',
        recipients=FEEDBACK_RECIPIENTS,
        charset='utf8',
        subject='Kerrokantasi palaute',
        body=feedback.content
    )
    mail.send(message)

    return jsonify({
        'feedback': {
            'id': feedback.id,
            'content': feedback.content
        }
    }), 201


def is_spam(json):
    return json.get('hp') is not None
