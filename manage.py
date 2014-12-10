#!/usr/bin/env python
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

import importlib

from flask import current_app
from flask.ext.failsafe import failsafe
from flask.ext.script import Manager, Server


@failsafe
def create_app():
    from kuulemma import Application
    return Application()


manager = Manager(create_app)
manager.add_command('runserver', Server(host='localhost'))


@manager.shell
def make_shell_context():
    from kuulemma.extensions import db

    context = {}
    context['app'] = current_app
    context['db'] = db
    context.update(db.Model._decl_class_registry)

    return context


@manager.command
def run(script):
    """Runs script from scripts folder in the application context.

    Example: python manage.py run hearing.add_hameentie"""
    module, function = script.rsplit('.', 1)
    if not module.startswith('scripts.'):
        module = 'scripts.%s' % module
    module = importlib.import_module(module)
    function = getattr(module, function)
    function()


@manager.command
def add_sample_data():
    """
        Generates 5 hearings with randomized starting and closing dates.
        Adds random number of comments to each hearing.
    """
    from kuulemma.extensions import db
    from kuulemma.sample_data import get_sample_hearing

    print('Start running script.')
    for _ in range(5):
        db.session.add(get_sample_hearing())
        print('Hearing added.')
    db.session.commit()
    print('Script completed succesfully.')


@manager.command
def add_user():
    from kuulemma.extensions import db
    from kuulemma.models import User

    user = User(
        email='john@fastmonkeys.com',
        username='john',
        password='john1234',
        is_admin=True,
        is_official=True
    )
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
