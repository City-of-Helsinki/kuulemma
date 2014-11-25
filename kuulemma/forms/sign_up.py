# -*- coding: utf-8 -*-
from wtforms_components import EmailField

from kuulemma.forms import Form
from kuulemma.models import User
from wtforms.fields import PasswordField, TextField
from wtforms.validators import Length, Required, ValidationError


class SignUpForm(Form):
    email = EmailField(u'Sähköpostiosoite', validators=[Required()])
    username = TextField(
        u'Käyttäjänimi', validators=[Required(), Length(min=4, max=100)]
    )
    password = PasswordField(
        u'Salasana', validators=[Required(), Length(min=6, max=100)]
    )

    def validate_email(self, field):
        if User.query.filter(User.email == field.data).count() != 0:
            raise ValidationError(u'Sähköposti jo käytössä.')

    def validate_username(self, field):
        if User.query.filter(User.username == field.data).count() != 0:
            raise ValidationError(u'Käyttäjänimi jo käytössä.')
