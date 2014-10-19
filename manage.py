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


if __name__ == '__main__':
    manager.run()
