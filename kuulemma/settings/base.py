# -*- coding: utf-8 -*-
"""
    kuulemma.settings.base
    ~~~~~~~~~~~~~~~~~~~~

    This module contains global application settings that are common to
    all environments.
"""
import os
from datetime import timedelta

#
# Paths
# -----

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)


#
# Generic
# -------

# Controls if the cookie should be set with the httponly flag. Defaults
# to ``True``.
SESSION_COOKIE_HTTPONLY = True


#
# Babel
# -----

# The default locale to use if no locale selector is registered. This
# defaults to 'en'.
BABEL_DEFAULT_LOCALE = 'fi'

# The timezone to use for user facing dates. This defaults to 'UTC',
# which also is the timezone your application must use internally.
BABEL_DEFAULT_TIMEZONE = 'Europe/Helsinki'


#
# Flask-Login
# -----------

# The default time before the "remember me" cookie expires (defaults to
# 365 days).
REMEMBER_COOKIE_DURATION = timedelta(days=30)

# Whether the "remember me" cookie uses HttpOnly or not; defaults to
# ``False``.
REMEMBER_COOKIE_HTTPONLY = True


#
# SeaSurf
# -------

CSRF_COOKIE_HTTPONLY = True


#
# Sentry
# ------

# A sentry compatible DSN.
SENTRY_DSN = os.environ.get('SENTRY_DSN')

MAIL_DEFAULT_SENDER = 'No Reply <noreply@hel.fi>'
