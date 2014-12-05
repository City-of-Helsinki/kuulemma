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

from kuulemma.models import User
from tests.asserts.views import assert_redirects
from tests.factories import UserFactory
from tests.utils import login_user


@pytest.mark.usefixtures('database')
class SignUpGetTest(object):
    @pytest.fixture
    def response(self, client):
        return client.get(url_for('auth.sign_up'))


class TestSignUpGetWithoutLogin(SignUpGetTest):
    def test_status_code(self, response):
        assert response.status_code == 200

    @pytest.mark.usefixtures('request_ctx')
    def test_url(self):
        assert url_for('auth.sign_up') == '/rekisteroidy'


class TestSignUpGetWithLogin(SignUpGetTest):
    @pytest.fixture
    def login(self, client):
        login_user(client, UserFactory())

    def test_status_code(self, login, response):
        assert response.status_code == 302

    def test_redirects_to_home_page(self, login, response):
        redirect_url = url_for('frontpage.index', _external=False)
        assert_redirects(response, redirect_url)


class TestSignUpPost(object):
    @pytest.fixture
    def response(self, client, data):
        return client.post(
            url_for('auth.sign_up'),
            data=data
        )


@pytest.mark.usefixtures('database')
class TestSuccessfullSignUp(TestSignUpPost):
    @pytest.fixture
    def data(self):
        return {
            'email': 'john@doe.com',
            'username': 'johndoe',
            'password': 'password'
        }

    def test_status_code(self, response):
        assert 302

    def test_redirects_to_home_page(self, response):
        redirect_url = url_for('frontpage.index', _external=False)
        assert_redirects(response, redirect_url)

    def test_creates_user_to_db(self, response):
        assert User.query.count() == 1


@pytest.mark.usefixtures('database')
class TestUnSuccessfullSignUp(TestSignUpPost):
    @pytest.fixture
    def data(self):
        return {
            'email': 'john@doe.com',
            'username': '',
            'password': 'password'
        }

    def test_status_code(self, response):
        assert 200

    def test_does_not_create_use_to_db(self, response):
        assert User.query.count() == 0

    def test_error_message(self, response):
        message = 'Tämä kenttä on pakollinen.'
        assert message in response.data.decode('utf8')
