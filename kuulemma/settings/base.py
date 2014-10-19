# -*- coding: utf-8 -*-
"""
    kuulemma.settings.base
    ~~~~~~~~~~~~~~~~~~~~

    This module contains global application settings that are common to
    all environments.
"""
import os

#
# Paths
# -----

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)

#
# Sentry
# ------

# A sentry compatible DSN.
SENTRY_DSN = os.environ.get('SENTRY_DSN')

#
# Babel
# -----

# The default locale to use if no locale selector is registered. This
# defaults to 'en'.
BABEL_DEFAULT_LOCALE = 'fi'

# The timezone to use for user facing dates. This defaults to 'UTC',
# which also is the timezone your application must use internally.
BABEL_DEFAULT_TIMEZONE = 'Europe/Helsinki'
