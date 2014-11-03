# -*- coding: utf-8 -*-
from datetime import datetime

import pytest
from sqlalchemy_utils import assert_max_length, assert_non_nullable

from kuulemma.extensions import db
from tests.asserts.models import assert_unique
from tests.factories import UserFactory


class TestUser(object):
    @pytest.fixture(scope='class')
    def user(self):
        return UserFactory.build(
            email='user@example.com',
            username='Luke',
        )

    def test_repr(self, user):
        assert repr(user) == (
            "<User username='Luke', email='user@example.com'>"
        )

    def test_str(self, user):
        assert str(user) == 'user@example.com'


@pytest.mark.usefixtures('database')
class TestUserWithDatabase(object):
    @pytest.fixture
    def user(self):
        return UserFactory(
            email='user@example.com',
            username='Luke',
            password='nakki',
        )

    @pytest.mark.parametrize(
        'column_name',
        [
            'is_admin',
            'is_official',
            'email',
            'password',
            'date_joined',
            'last_seen',
            'username',
        ]
    )
    def test_non_nullable_columns(self, column_name, user):
        assert_non_nullable(user, column_name)

    def test_date_joined_defaults_to_datetime(self):
        assert isinstance(UserFactory(date_joined=None).date_joined, datetime)

    def test_last_seen_defaults_to_datetime(self):
        assert isinstance(UserFactory(last_seen=None).last_seen, datetime)

    def test_username_defaults_to_empty_string(self):
        assert UserFactory(username=None).username == ''

    def test_is_admin_defaults_to_false(self):
        assert UserFactory(is_admin=None).is_admin is False

    def test_is_official_defaults_to_false(self):
        assert UserFactory(is_official=None).is_official is False

    def test_username_max_length(self, user):
        assert_max_length(user, 'username', 255)

    def test_email_is_unique(self, user):
        assert_unique(UserFactory, 'email')

    def test_password_equal_with_valid_password(self, user):
        # The user password hash is calculated only on commit.
        db.session.commit()
        assert user.password == 'nakki'

    def test_password_unequal_with_invalid_password(self, user):
        # The user password hash is calculated only on commit.
        db.session.commit()
        assert not user.password == 'makkara'
