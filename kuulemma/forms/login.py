# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms.fields import PasswordField
from wtforms_components import EmailField


class LoginForm(Form):
    email = EmailField(u'Sähköpostiosoite')
    password = PasswordField(u'Salasana')
