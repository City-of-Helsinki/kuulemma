# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms.fields import PasswordField, TextField
from wtforms.validators import Length, Required, ValidationError
from wtforms_components import EmailField

from kuulemma.models import User

required = Required(message='Tämä kenttä on pakollinen.')


class SignUpForm(Form):
    email = EmailField(
        u'Sähköpostiosoite',
        validators=[Required(message='Sähköpostiosoite on pakollinen.')]
    )
    username = TextField(
        u'Käyttäjänimi', validators=[
            required,
            Length(
                min=4,
                max=100,
                message='Käyttäjänimi täytyy olla vähintään 4 merkkiä pitkä.'
            )
        ]
    )
    password = PasswordField(
        u'Salasana',
        validators=[
            required,
            Length(
                min=6,
                max=100,
                message='Salasana täytyy olla vähintään 6 merkkiä pitkä.'
            )
        ]
    )

    def validate_email(self, field):
        if User.query.filter(User.email == field.data).count() != 0:
            raise ValidationError(u'Sähköposti jo käytössä.')

    def validate_username(self, field):
        if User.query.filter(User.username == field.data).count() != 0:
            raise ValidationError(u'Käyttäjänimi jo käytössä.')
