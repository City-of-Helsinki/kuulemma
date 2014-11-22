from flask import current_app
from flask.ext import wtf
from flask.ext.babel import get_locale

from wtforms.ext.i18n.utils import get_translations


class Form(wtf.Form):
    translations_cache = {}
    csrf_enabled = False

    def _get_translations(self):
        locale = get_locale()
        if not locale:
            return None
        fallback_language = current_app.config['BABEL_DEFAULT_LOCALE']
        languages = (locale.language, fallback_language)
        if languages not in self.translations_cache:
            self.translations_cache[languages] = get_translations(languages)
        return self.translations_cache[languages]
