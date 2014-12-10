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

import contextlib

import pytest
from flask import _app_ctx_stack, _request_ctx_stack, json, Response
from sqlalchemy import event
from sqlalchemy.pool import Pool
from werkzeug import cached_property

from kuulemma import Application
from kuulemma.extensions import db


class DatabaseGuard(object):
    def __init__(self, enabled=True):
        self.enabled = True
        event.listen(Pool, 'connect', self.on_connect)

    def on_connect(self, dbapi_connection, connection_record):
        if self.enabled:
            raise Exception(
                'Test cases that are not marked that they use database '
                'should not use database.'
            )

    @contextlib.contextmanager
    def disabled(self):
        was_enabled = self.enabled
        self.enabled = False
        yield
        self.enabled = was_enabled


@pytest.fixture(scope='session', autouse=True)
def database_guard():
    """
    Prevent database access from tests not marked to use database

    We want to do this as otherwise our connection pool is not disposed
    and connection to database server stays alive and may cause
    problems.
    """
    return DatabaseGuard()


class TestResponse(Response):
    @cached_property
    def json(self):
        return json.loads(self.data)


@pytest.fixture(scope='session')
def app(request):
    app = Application('test')
    app.response_class = TestResponse

    ctx = app.app_context()
    ctx.push()
    request.addfinalizer(ctx.pop)

    return app


@pytest.fixture
def app_ctx(request, app):
    ctx = app.app_context()
    ctx.push()
    request.addfinalizer(ctx.pop)
    return ctx


@pytest.fixture(scope='class')
def app_ctx_in_class_scope(request, app):
    return app_ctx(request, app)


@pytest.yield_fixture
def request_ctx(request, app):
    ctx = app.test_request_context()
    ctx.push()
    yield ctx
    if _request_ctx_stack.top and _request_ctx_stack.top.preserved:
        _request_ctx_stack.top.pop()
    ctx.pop()


@pytest.fixture(scope='session')
def client(request, app):
    return app.test_client()


@pytest.yield_fixture(scope='session')
def database_schema(request, app, database_guard):
    with database_guard.disabled(), app.app_context():
        db.session.execute('CREATE EXTENSION IF NOT EXISTS postgis')
        db.session.commit()
        db.create_all()

    yield

    with database_guard.disabled(), app.app_context():
        db.drop_all()


def _database(database_guard):
    with database_guard.disabled():
        yield

        db.session.remove()

        # Delete all data from tables.
        tables = reversed(db.metadata.sorted_tables)
        for table in tables:
            db.session.execute(table.delete())
        db.session.commit()

        db.session.close_all()
        db.engine.dispose()

    _app_ctx_stack.top.sqlalchemy_queries = []


@pytest.yield_fixture
def database(database_schema, database_guard, app_ctx):
    for x in _database(database_guard):
        yield x


@pytest.yield_fixture(scope='class')
def database_in_class_scope(
    database_schema, database_guard, app_ctx_in_class_scope
):
    for x in _database(database_guard):
        yield x


@pytest.yield_fixture(scope='module')
def database_in_module_scope(
    database_schema, database_guard, app_ctx_in_module_scope
):
    for x in _database(database_guard):
        yield x
