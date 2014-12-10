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
            'username': ['Tämä kenttä on pakollinen.'],
            'password': ['Tämä kenttä on pakollinen.']
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
