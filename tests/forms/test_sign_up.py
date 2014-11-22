import pytest
from werkzeug.datastructures import MultiDict

from kuulemma.forms.sign_up import SignUpForm
from tests.factories import UserFactory


@pytest.mark.usefixtures('database', 'request_ctx')
class TestSignUpFormValidation(object):
    def test_without_data_should_not_validate(self):
        form = SignUpForm()
        assert not form.validate()

        assert form.errors == {
            'email': ['Sähköpostiosoite on pakollinen.'],
            'username': ['Käyttäjänimi on pakollinen.'],
            'password': ['Salasana on pakollinen.']
        }

    def test_should_validate_when_all_data_present(self):
        data = MultiDict([
            ('email', 'john@doe.com'),
            ('username', 'johndoe'),
            ('password', 'password'),
        ])
        form = SignUpForm(data)
        assert form.validate()
        assert form.errors == {}

    def test_should_not_validate_if_not_unique_email(self):
        UserFactory(email='john@doe.com')
        data = MultiDict([
            ('email', 'john@doe.com'),
            ('username', 'johndoe'),
            ('password', 'password'),
        ])
        form = SignUpForm(data)
        assert not form.validate()
        assert form.errors == {'email': ['Sähköposti jo käytössä.']}

    def test_should_not_validate_if_not_unique_username(self):
        UserFactory(username='johndoe')
        data = MultiDict([
            ('email', 'john@doe.com'),
            ('username', 'johndoe'),
            ('password', 'password')
        ])
        form = SignUpForm(data)
        assert not form.validate()
        assert form.errors == {'username': ['Käyttäjänimi jo käytössä.']}
