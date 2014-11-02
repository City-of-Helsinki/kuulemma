# -*- coding: utf-8 -*-
import pytest
from flask import url_for
from flask.ext.login import current_user

from kuulemma.extensions import db
from tests.asserts.views import assert_redirects
from tests.factories import UserFactory


@pytest.mark.usefixtures('database')
class LoginTestCase(object):
    @pytest.fixture(scope='class')
    def password(self):
        return 'password'

    @pytest.fixture
    def response(self, client, data):
        return client.post(
            url_for('auth.login'),
            data=data
        )

    @pytest.fixture
    def user(self, password):
        user = UserFactory(password=password)
        # The user password hash is calculated only on commit.
        db.session.commit()
        return user


@pytest.mark.usefixtures('request_ctx')
def test_login_url():
    assert (
        url_for('auth.login') == '/kirjaudu-sisaan'
    )


class TestSuccessfullLogin(LoginTestCase):
    @pytest.fixture
    def data(self, user, password):
        return {
            'email': user.email,
            'password': password,
        }

    def test_logs_the_user_in(self, client, data, user):
        with client:
            client.post(url_for('auth.login'), data=data)
            assert current_user == user

    def test_redirects_to_home_page(self, response):
        redirect_url = url_for('frontpage.index', _external=False)
        assert_redirects(response, redirect_url)


class TestInvalidEmailLogin(LoginTestCase):
    @pytest.fixture
    def data(self, user, password):
        return {
            'email': 'invalid_email',
            'password': password,
        }

    def test_status_code_should_be_200(self, response):
        assert response.status_code == 200

    def test_should_not_log_the_user_in(self, response, user):
        assert current_user != user

    def test_shows_error_message(self, response):
        message = 'Syöttämäsi sähköpostiosoite ja salasana eivät täsmää.'
        assert message in response.data.decode('utf8')


class TestInvalidPasswordLogin(LoginTestCase):
    @pytest.fixture
    def data(self, user):
        return {
            'email': user.email,
            'password': u'invalid_password',
        }

    def test_status_code_should_be_200(self, response):
        assert response.status_code == 200

    def test_should_not_log_the_user_in(self, response, user):
        assert current_user != user

    def test_shows_error_message(self, response):
        message = 'Syöttämäsi sähköpostiosoite ja salasana eivät täsmää.'
        assert message in response.data.decode('utf8')
