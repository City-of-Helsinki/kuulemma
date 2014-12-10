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

from flask import current_app, render_template, url_for
from flask.ext.mail import Message

from kuulemma.extensions import mail
from kuulemma.serializers import account_activation_serializer


def send_registration_mail(user):
    email_hash = account_activation_serializer.dumps(user.email)

    confirmation_url = (
        'https://kerrokantasi.hel.fi' +
        url_for('auth.activate_account', activation_hash=email_hash)
    )
    with current_app.test_request_context():
        context = {
            'user': user,
            'confirmation_url': confirmation_url,
        }
        message = Message(
            recipients=[user.email],
            charset='utf8',
            subject=render_template(
                'email/registration_subject.txt'
            ),
            body=render_template(
                'email/registration.txt',
                **context
            ).encode('utf8')
        )
        mail.send(message)
