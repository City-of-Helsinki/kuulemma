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

from kuulemma.models import Like
from tests.factories import CommentFactory, LikeFactory, UserFactory
from tests.utils import login_user


@pytest.mark.usefixtures('request_ctx')
def test_create_like_url():
    assert (
        url_for('like.create', user_id=1) ==
        '/users/1/links/likes'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class CreateLikeTestCase(object):
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def comment(self):
        return CommentFactory()

    @pytest.fixture
    def create_data(self, comment):
        return {'comment_id': comment.id}


class TestCreateLikeOnSuccess(CreateLikeTestCase):
    @pytest.fixture
    def response(self, client, user, create_data):
        login_user(client, user)
        return client.post(
            url_for('like.create', user_id=user.id),
            data=json.dumps(create_data),
            content_type='application/json'
        )

    def test_returns_201(self, response):
        assert response.status_code == 201

    def test_returns_the_number_of_likes(self, response, create_data, comment):
        content = response.data.decode('utf8')
        expected = '"like_count": {like_count}'.format(
            like_count=comment.like_count
        )
        assert expected in content

    def test_creates_a_new_like(self, response):
        assert len(Like.query.all()) == 1

    def test_attaches_like_to_the_right_comment(self, response, comment):
        like = Like.query.first()
        assert like in comment.likes

    def test_attaches_like_to_the_right_user(self, response, user):
        like = Like.query.first()
        assert like in user.likes


class TestCreateLikeOnError(CreateLikeTestCase):
    @pytest.fixture
    def response(self, client, user, comment):
        LikeFactory(user=user, comment=comment)
        login_user(client, user)
        return client.post(
            url_for('like.create', user_id=user.id),
            data=json.dumps({'comment_id': comment.id}),
            content_type='application/json'
        )

    def test_returns_404_for_non_existent_user(self, client):
        response = client.post(
            url_for('like.create', user_id=999)
        )
        assert response.status_code == 404

    def test_returns_404_for_non_existent_comment(self, client, user):
        login_user(client, user)
        response = client.post(
            url_for('like.create', user_id=user.id),
            data=json.dumps({'comment_id': 999}),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_returns_401_if_user_is_not_logged_in(
        self, client, user, create_data
    ):
        response = client.post(
            url_for('like.create', user_id=user.id),
            data=json.dumps(create_data),
            content_type='application/json'
        )
        assert response.status_code == 401

    def test_returns_400_if_like_already_exists(self, response):
        assert response.status_code == 400

    def test_returns_error_message_if_like_already_exists(self, response):
        message = 'User has already liked the comment.'
        assert message in response.data.decode('utf8')
