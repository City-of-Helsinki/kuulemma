import pytest
from flask import url_for

from kuulemma.models import User
from kuulemma.serializers import account_activation_serializer
from tests.factories import UserFactory


@pytest.mark.usefixtures('database')
class ActivateAccountTest(object):
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def activation_hash(self, user):
        return account_activation_serializer.dumps(user.email)

    @pytest.fixture
    def response(self, client, activation_hash):
        return client.get(
            url_for(
                'auth.activate_account',
                activation_hash=activation_hash
            ),
            follow_redirects=True,
        )


class TestActivateAccountWithCorrectLink(ActivateAccountTest):
    def test_should_return_200(self, response):
        assert response.status_code == 200

    def test_should_correct_flash_message(self, response):
        message = 'Tilisi on aktivoitu'
        assert message in response.data.decode('utf8')

    def test_should_activate_account(self, user, response):
        assert User.query.get(user.id).active


class TestActivateAccountWithAlreadyActivatedUser(ActivateAccountTest):
    @pytest.fixture
    def user(self):
        return UserFactory(active=True)

    def test_should_return_200(self, response):
        assert response.status_code == 200

    def test_should_return_correct_error_flash(self, response):
        message = 'Olet jo aktivoinut tilisi.'
        assert message in response.data.decode('utf8')


class TestActivateAccountWithWrongHash(ActivateAccountTest):
    @pytest.fixture
    def activation_hash(self):
        return 'random'

    def test_should_return_200(self, response):
        assert response.status_code == 200

    def test_should_return_correct_error_flash(self, response):
        message = 'Tarkista osoite'
        assert message in response.data.decode('utf8')
