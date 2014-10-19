# -*- coding: utf-8 -*-
"""
    kuulemma.settings.test
    ~~~~~~~~~~~~~~~~~~~~~~

    This module contains application settings specific to a automated
    tests.
"""

from .base import *  # noqa

#
# Generic
# -------

# If a secret key is set, cryptographic components can use this to sign cookies
# and other things. Set this to a complex random value when you want to use the
# secure cookie for instance.
SECRET_KEY = 'development key'

SERVER_NAME = 'localhost'

# The debug flag. Set this to True to enable debugging of the application. In
# debug mode the debugger will kick in when an unhandled exception ocurrs and
# the integrated server will automatically reload the application if changes in
# the code are detected.
DEBUG = True

TESTING = True

LOGIN_DISABLED = False

#
# SQLAlchemy
# ----------

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'TEST_DATABASE_URL',
    'postgres://localhost/kuulemma_test'
)

#
# Mail
# ----

MAIL_SUPPRESS_SEND = True
