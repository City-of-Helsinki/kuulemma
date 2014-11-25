from flask.ext.babel import Babel
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from raven.contrib.flask import Sentry
from sqlalchemy_continuum import make_versioned

csrf = CsrfProtect()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
sentry = Sentry()
babel = Babel()

make_versioned(user_cls=None)
