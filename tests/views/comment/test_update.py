import json
from datetime import datetime

import pytest
from flask import url_for
from freezegun import freeze_time

from tests.factories import CommentFactory, HearingFactory, UserFactory
from tests.utils import login_user


@pytest.mark.usefixtures('request_ctx')
def test_delete_like_url():
    assert (
        url_for('comment.update', hearing_id=1, comment_id=1) ==
        '/hearings/1/links/comments/1'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestUpdateCommentOnSuccess(object):
    @pytest.fixture
    def user(self):
        return UserFactory(is_official=True)

    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.fixture
    def comment(self, hearing):
        return CommentFactory(hearing=hearing)

    @pytest.fixture
    def comment_data(self, hearing):
        return {
            'title': 'Updated title',
            'body': 'Updated body',
            'username': 'New username',
            'is_hidden': True
        }

    @pytest.fixture
    @freeze_time('2012-01-14 12:00:00')
    def response(self, client, user, hearing, comment, comment_data):
        login_user(client, user)
        return client.put(
            url_for(
                'comment.update',
                hearing_id=hearing.id,
                comment_id=comment.id
            ),
            data=json.dumps(comment_data),
            content_type='application/json'
        )

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_returns_comment_data(self, response, comment):
        content = response.data.decode('utf8')
        assert str(comment.id) in content
        assert comment.title in content
        assert comment.body in content

    @freeze_time('2012-01-14 12:00:00')
    def test_updates_updated_at_value(self, response, comment):
        assert comment.updated_at == datetime.utcnow()

    def test_updates_title(self, response, comment, comment_data):
        assert comment.title == comment_data['title']

    def test_updates_body(self, response, comment, comment_data):
        assert comment.body == comment_data['body']

    def test_updates_username(self, response, comment, comment_data):
        assert comment.username == comment_data['username']

    def test_updates_is_hidden_value(self, response, comment):
        assert comment.is_hidden


@pytest.mark.usefixtures('database', 'request_ctx')
class TestUpdateCommentOnError(object):
    @pytest.fixture
    def user(self):
        return UserFactory()

    @pytest.fixture
    def official(self):
        return UserFactory(is_official=True)

    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.fixture
    def comment(self, hearing):
        return CommentFactory(hearing=hearing)

    def test_returns_401_if_user_is_unauthenticated(
        self, client, hearing, comment
    ):
        response = client.put(
            url_for(
                'comment.update',
                hearing_id=hearing.id,
                comment_id=comment.id
            )
        )
        assert response.status_code == 401

    def test_returns_401_for_non_officials(
        self, client, user, hearing, comment
    ):
        login_user(client, user)
        response = client.put(
            url_for(
                'comment.update',
                hearing_id=hearing.id,
                comment_id=comment.id
            )
        )
        assert response.status_code == 401

    def test_returns_404_for_non_existing_hearing(
        self, client, official, hearing, comment
    ):
        login_user(client, official)
        response = client.put(
            url_for(
                'comment.update',
                hearing_id=999,
                comment_id=comment.id
            )
        )
        assert response.status_code == 404

    def test_returns_404_for_non_existing_comment(
        self, client, official, hearing, comment
    ):
        login_user(client, official)
        response = client.put(
            url_for(
                'comment.update',
                hearing_id=hearing.id,
                comment_id=999
            )
        )
        assert response.status_code == 404

    def test_returns_400_if_data_is_not_json(
        self, client, official, hearing, comment
    ):
        login_user(client, official)
        response = client.put(
            url_for(
                'comment.update',
                hearing_id=hearing.id,
                comment_id=comment.id
            )
        )
        assert response.status_code == 400
