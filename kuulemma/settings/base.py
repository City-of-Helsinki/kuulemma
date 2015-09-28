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


#
# Mail
# ----

MAIL_DEFAULT_SENDER = 'No Reply <noreply@hel.fi>'

FEEDBACK_RECIPIENTS = [
    'joonas.pekkanen@hel.fi',
    'riku.oja@hel.fi'
]


#
# Analytics
#

PIWIK_ON = False
