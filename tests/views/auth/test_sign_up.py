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
        message = 'Käyttäjänimi on pakollinen.'
        assert message in response.data.decode('utf8')
