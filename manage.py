#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
def add_sample_data():
    """
        Generates 5 hearings with randomized starting and closing dates.
        Adds random number of comments to each hearing.
    """
    from kuulemma.extensions import db
    from kuulemma.sample_data import get_sample_hearing

    for _ in range(5):
        db.session.add(get_sample_hearing())
    db.session.commit()


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
