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
    kuulemma
    ~~~~~~~~

    This module contains the Flask application core.
"""
import os
import warnings

from flask import current_app, Flask, json
from flask.ext.login import current_user
from sqlalchemy.exc import SAWarning

from .extensions import babel, csrf, db, login_manager, mail, sentry

warnings.simplefilter('error', SAWarning)


class Application(Flask):
    def __init__(self, environment=None):
        super(Application, self).__init__(__name__)
        self._init_settings(environment)
        self._init_extensions()
        self._init_blueprints()

    def _init_settings(self, environment=None):
        """
        Initialize application configuration.

        This method loads the configuration from the given environment
        (production, development, test).  If no environment is given as an
        argument, the environment is read from ``FLASK_ENV`` environmental
        variable.  If ``FLASK_ENV`` is not defined, the environment defaults to
        development.

        The environment specific configuration is loaded from the module
        corresponding to the environment in :module:`.settings`.

        :param environment: the application environment
        """
        if environment is None:
            environment = os.environ.get('FLASK_ENV', 'development')
        settings_module = 'kuulemma.settings.' + environment
        self.config.from_object(settings_module)

        @self.context_processor
        def inject_settings():
            return dict(PIWIK_ON=self.config.get('PIWIK_ON'))

    def _init_blueprints(self):
        from .views.auth import auth
        from .views.comment import comment
        from .views.feedback import feedback
        from .views.frontpage import frontpage
        from .views.hearing import hearing
        from .views.like import like
        from .views.static_pages import static_pages

        self.register_blueprint(auth)
        self.register_blueprint(comment)
        self.register_blueprint(feedback)
        self.register_blueprint(frontpage)
        self.register_blueprint(hearing)
        self.register_blueprint(like)
        self.register_blueprint(static_pages)

    def _init_extensions(self):
        """Initialize and configure Flask extensions with this application."""
        csrf.init_app(self)
        db.init_app(self)
        login_manager.init_app(self)
        babel.init_app(self)
        self._init_babel()
        self._init_raven()
        mail.init_app(self)

    def _init_raven(self):
        from raven.conf import EXCLUDE_LOGGER_DEFAULTS, setup_logging
        from raven.handlers.logging import SentryHandler

        # Initialize Raven only if SENTRY_DSN setting is defined.
        if not self.config.get('SENTRY_DSN'):
            return

        sentry.init_app(self)
        handler = SentryHandler(sentry.client)

        setup_logging(handler, exclude=EXCLUDE_LOGGER_DEFAULTS + (
            'celery',
            'requests',
        ))

    def _init_babel(self):
        @babel.localeselector
        def get_locale():
            """
            Get the locale to use for the response.
            """
            from flask import session

            try:
                if current_user.is_authenticated():
                    session['locale'] = current_user.locale
            except AttributeError:
                # Don't crash if current_user is not defined (for
                # example when not within request context).
                pass

            if 'locale' in session:
                return session['locale']

            return babel.default_locale.language

    def create_jinja_environment(self):
        rv = super(Application, self).create_jinja_environment()
        rv.globals.update(get_asset_path=get_asset_path)
        return rv


def get_asset_path(asset_type, filename):
    manifest_filename = os.path.join(
        current_app.static_folder,
        'dist',
        asset_type,
        'rev-manifest.json'
    )
    try:
        with current_app.open_resource(manifest_filename, 'rb') as manifest:
            data = json.load(manifest)
            asset_filename = os.path.join('dist', asset_type, data[filename])
            return asset_filename
    except FileNotFoundError:
        return os.path.join('dist', asset_type, filename)
