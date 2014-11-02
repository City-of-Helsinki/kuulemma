import json

import pytest
from flask import url_for

from kuulemma.models import Like
from tests.factories import CommentFactory, LikeFactory, UserFactory
from tests.utils import login_user


@pytest.mark.usefixtures('request_ctx')
def test_like_url():
    assert (
        url_for('comment.like', comment_id=1) ==
        '/comments/1/links/likes'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class LikeTestCase(object):
    @pytest.fixture(scope='function')
    def user(self):
        return UserFactory()

    @pytest.fixture(scope='function')
    def comment(self):
        return CommentFactory()

    @pytest.fixture(scope='function')
    def like_data(self, user):
        return {'user_id': user.id}


class TestCreateLikeOnSuccess(LikeTestCase):
    @pytest.fixture(scope='function')
    def response(self, client, user, comment, like_data):
        login_user(client, user)
        return client.post(
            url_for('comment.like', comment_id=comment.id),
            data=json.dumps(like_data),
            content_type='application/json'
        )

    def test_returns_201(self, response):
        assert response.status_code == 201

    def test_returns_the_number_of_likes(self, response, like_data, comment):
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


class TestRemoveLikeOnSuccess(LikeTestCase):
    @pytest.fixture
    def like(self, user, comment):
        return LikeFactory(user=user, comment=comment)

    @pytest.fixture
    def response(self, client, user, comment, like_data):
        login_user(client, user)
        return client.post(
            url_for('comment.like', comment_id=comment.id),
            data=json.dumps(like_data),
            content_type='application/json'
        )

    def test_removes_like_if_it_exists(
        self, client, comment, user, like, like_data
    ):
        assert len(comment.likes) == 1
        login_user(client, user)
        client.post(
            url_for('comment.like', comment_id=comment.id),
            data=json.dumps(like_data),
            content_type='application/json'
        )
        assert len(comment.likes) == 0


class TestCreateLikeOnError(LikeTestCase):
    @pytest.fixture(scope='function')
    def response(self, client, user, comment, like_data):
        return client.post(
            url_for('comment.like', comment_id=comment.id),
            data=json.dumps(like_data),
            content_type='application/json'
        )

    def test_returns_404_for_non_existent_comment(self, client):
        response = client.post(
            url_for('comment.like', comment_id=999)
        )
        assert response.status_code == 404

    def test_returns_404_for_non_existent_user(self, client, comment):
        response = client.post(
            url_for('comment.like', comment_id=comment.id),
            data=json.dumps({'user_id': 999}),
            content_type='application/json'
        )
        assert response.status_code == 404

    def test_returns_401_if_user_is_not_logged_in(self, response):
        assert response.status_code == 401
