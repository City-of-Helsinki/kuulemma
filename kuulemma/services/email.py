# -*- coding: utf-8 -*-
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
