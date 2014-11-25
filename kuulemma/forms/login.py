# -*- coding: utf-8 -*-
from wtforms_components import EmailField

from kuulemma.forms import Form
from wtforms.fields import PasswordField


class LoginForm(Form):
    email = EmailField(u'Sähköpostiosoite')
    password = PasswordField(u'Salasana')
