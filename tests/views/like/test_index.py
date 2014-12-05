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

import json

import pytest
from flask import url_for

from tests.factories import LikeFactory, UserFactory
from tests.utils import login_user


@pytest.mark.usefixtures('request_ctx')
def test_index_url():
    assert (
        url_for('like.index', user_id=1) ==
        '/users/1/links/likes'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestIndexOnSuccess(object):
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def like(self, user):
        return LikeFactory(user=user)

    @pytest.fixture
    def response(self, client, user, like):
        login_user(client, user)
        return client.get(
            url_for('like.index', user_id=user.id)
        )

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_returns_list_of_liked_comment_ids(
        self, response, like
    ):
        content = response.data.decode('utf8')
        assert str(like.comment_id) in content

    def test_returns_empty_list_if_there_are_no_likes(self, client):
        another_user = UserFactory()
        login_user(client, another_user)
        response = client.get(
            url_for('like.index', user_id=another_user.id)
        )
        content = response.data.decode('utf8')
        assert '[]' in content


@pytest.mark.usefixtures('database', 'request_ctx')
class TestIndexOnError(object):
    @pytest.fixture
    def user(self):
        return UserFactory()

    def test_returns_404_if_user_does_not_exist(self, client):
        response = client.get(
            url_for('like.index', user_id=999)
        )
        assert response.status_code == 404

    def test_returns_401_if_user_is_not_authenticated(self, client, user):
        response = client.get(
            url_for('like.index', user_id=user.id)
        )
        assert response.status_code == 401

    def test_returns_404_if_hearing_does_not_exist(self, client, user):
        login_user(client, user)
        response = client.get(
            url_for('like.index', user_id=user.id),
            data=json.dumps({'hearing_id': 999}),
            content_type='application/json'
        )
        assert response.status_code == 404
