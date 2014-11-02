import json

import pytest
from flask import url_for

from tests.factories import CommentFactory, LikeFactory, UserFactory
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
    def comment(self):
        return CommentFactory()

    @pytest.fixture
    def delete_data(self, comment):
        return {'comment_id': comment.id}


class TestDeleteLikeOnSuccess(DeleteLikeTestCase):
    @pytest.fixture
    def like(self, user, comment):
        return LikeFactory(user=user, comment=comment)

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


class TestDeleteLikeOnError(DeleteLikeTestCase):
    @pytest.fixture
    def response(self, client, user, delete_data):
        return client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps(delete_data),
            content_type='application/json'
        )

    def test_returns_404_for_non_existent_user(self, client):
        response = client.delete(
            url_for('like.delete', user_id=999)
        )
        assert response.status_code == 404

    def test_returns_400_for_non_existent_comment(self, client, user):
        login_user(client, user)
        response = client.delete(
            url_for('like.delete', user_id=user.id),
            data=json.dumps({'comment_id': 999}),
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_returns_401_if_user_is_not_logged_in(self, response):
        assert response.status_code == 401
