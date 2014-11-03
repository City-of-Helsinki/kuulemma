# -*- coding: utf-8 -*-
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
