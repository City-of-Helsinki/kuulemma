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
from datetime import date, timedelta

import pytest
from flask import url_for

from kuulemma.extensions import db
from tests.factories import (
    CommentFactory,
    HearingFactory,
    LikeFactory,
    UserFactory
)
from tests.utils import login_user


@pytest.mark.usefixtures('request_ctx')
def test_delete_like_url():
    assert (
        url_for('like.delete', user_id=1) ==
        '/users/1/links/likes'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class DeleteLikeTestCase(object):
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def hearing(self):
        return HearingFactory(closes_at=date.today() + timedelta(2))

    @pytest.fixture
    def comment(self, hearing):
        return CommentFactory(hearing=hearing)

    @pytest.fixture
    def delete_data(self, comment):
        return {'comment_id': comment.id}

    @pytest.fixture
    def like(self, user, comment):
        return LikeFactory(user=user, comment=comment)


class TestDeleteLikeOnSuccess(DeleteLikeTestCase):
    @pytest.fixture
    def response(self, client, user, comment, delete_data, like):
        login_user(client, user)
        return client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps(delete_data),
            content_type='application/json'
        )

    def test_returns_204(self, response):
        assert response.status_code == 204

    def test_returns_empty_string_in_body(self, response, comment):
        content = response.data.decode('utf8')
        assert content == ''

    def test_deletes_like(
        self, client, comment, user, like, delete_data
    ):
        assert len(user.likes) == 1
        login_user(client, user)
        client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps(delete_data),
            content_type='application/json'
        )
        assert len(user.likes) == 0

    def test_decreases_comment_like_count(
        self, client, comment, user, like, delete_data
    ):
        db.session.commit()
        assert comment.like_count == 1
        login_user(client, user)
        client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps(delete_data),
            content_type='application/json'
        )
        assert comment.like_count == 0


class TestDeleteLikeOnError(DeleteLikeTestCase):
    def test_returns_404_for_non_existent_user(self, client):
        response = client.delete(
            url_for('like.delete', user_id=999)
        )
        assert response.status_code == 404

    def test_returns_401_if_user_is_not_logged_in(
        self, client, user, comment, like
    ):
        response = client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps({'comment_id': comment.id}),
            content_type='application/json'
        )
        assert response.status_code == 401

    def test_returns_404_for_non_existent_comment(self, client, user, like):
        login_user(client, user)
        response = client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps({'comment_id': 999}),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_returns_400_for_non_existent_like(self, client, user, comment):
        login_user(client, user)
        response = client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps({'comment_id': comment.id}),
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_returns_400_if_hearing_is_closed(self, client, user):
        login_user(client, user)
        hearing = HearingFactory(closes_at=date.today() - timedelta(2))
        comment = CommentFactory(hearing=hearing)
        LikeFactory(user=user, comment=comment)
        response = client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps({'comment_id': comment.id}),
            content_type='application/json'
        )
        assert response.status_code == 400
