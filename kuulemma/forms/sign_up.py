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
from flask_wtf import Form
from wtforms.fields import PasswordField, TextField
from wtforms.validators import Email, Length, Required, ValidationError
from wtforms_components import EmailField

from kuulemma.models import User

required = Required(message='Tämä kenttä on pakollinen.')


class SignUpForm(Form):
    email = EmailField(
        u'Sähköpostiosoite',
        validators=[
            Required(message='Sähköpostiosoite on pakollinen.'),
            Email(message='Sähköpostiosoitteen täytyy sisältää @ ja . merkit.')
        ]
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
