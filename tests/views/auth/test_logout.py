# -*- coding: utf-8 -*-
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
        return UserFactory()

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
