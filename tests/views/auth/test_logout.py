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

import pytest
from flask import url_for
from flask.ext.login import current_user, login_user

from tests.asserts.views import assert_redirects
from tests.factories import UserFactory


@pytest.mark.usefixtures('request_ctx')
def test_logout_url():
    assert (
        url_for('auth.logout') == '/kirjaudu-ulos'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestLogout(object):
    @pytest.fixture(scope='class')
    def user(self):
        return UserFactory(active=True)

    @pytest.fixture(scope='class')
    def login(self, client, user):
        with client:
            login_user(user, remember=True)

    def test_user_gets_logged_out(self, client, user):
        with client:
            login_user(user, remember=True)
            assert current_user.is_authenticated()

            client.get(url_for('auth.logout'))
            assert not current_user.is_authenticated()

    def test_redirects_home(self, client, login, user):
        response = client.get(url_for('auth.logout'))
        redirect_url = url_for('frontpage.index', _external=False)
        assert_redirects(response, redirect_url)
