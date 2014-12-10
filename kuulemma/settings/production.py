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

"""
    kuulemma.settings.production
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains application settings specific to a production
    environment.
"""

import os

from .base import *  # noqa

#
# Generic
# -------

# If a secret key is set, cryptographic components can use this to sign cookies
# and other things. Set this to a complex random value when you want to use the
# secure cookie for instance.
SECRET_KEY = os.environ['SECRET_KEY']

# The debug flag. Set this to True to enable debugging of the application. In
# debug mode the debugger will kick in when an unhandled exception ocurrs and
# the integrated server will automatically reload the application if changes in
# the code are detected.
DEBUG = 'DEBUG' in os.environ

# Controls if the cookie should be set with the secure flag. Defaults
# to ``False``.
SESSION_COOKIE_SECURE = True

#
# Flask-Login
# -----------

# Whether the "remember me" cookie requires Secure; defaults to
# ``None``.
REMEMBER_COOKIE_SECURE = True


#
# Mail
# ----

MAIL_SERVER = os.environ['MAIL_SERVER']
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
MAIL_PORT = os.environ['MAIL_PORT']
MAIL_USE_TLS = True


#
# SeaSurf
# -------

CSRF_COOKIE_SECURE = True


#
# SQLAlchemy
# ----------

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


#
# Analytics
#

PIWIK_ON = True
