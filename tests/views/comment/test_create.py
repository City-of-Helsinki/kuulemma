import json

import pytest
from flask import url_for

from kuulemma.models import Comment
from tests.factories import HearingFactory


@pytest.mark.usefixtures('request_ctx')
def test_create_url():
    assert (
        url_for('comment.create', hearing_id=1) ==
        '/hearings/1/links/comments'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCreateCommentOnSuccess(object):
    @pytest.fixture(scope='class')
    def comment_data(self):
        return {
            'title': 'Hello World!',
            'body': 'I really don\'t like this death star idea!',
            'username': 'Luke Skywalker'
        }

    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.fixture
    def response(self, client, hearing, comment_data):
        return client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )

    def test_returns_201(self, response):
        assert response.status_code == 201

    def test_returns_the_created_comment(self, response, comment_data):
        content = response.data.decode('utf8')
        assert comment_data['title'] in content
        assert comment_data['username'] in content

    def test_creates_a_new_comment(self, response):
        assert len(Comment.query.all()) == 1

    def test_saves_title(self, response, comment_data):
        comment = Comment.query.first()
        assert comment.title == comment_data['title']

    def test_saves_username(self, response, comment_data):
        comment = Comment.query.first()
        assert comment.username == comment_data['username']

    def test_saves_body(self, response, comment_data):
        comment = Comment.query.first()
        assert comment.body == comment_data['body']

    def test_attaches_comment_to_the_right_hearing(self, response, hearing):
        comment = Comment.query.first()
        assert comment.hearing == hearing


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCreateCommentOnError(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.fixture
    def no_hearing_response(self, client):
        return client.post(
            url_for('comment.create', hearing_id=999)
        )

    @pytest.fixture
    def missing_data_response(self, client, hearing):
        return client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps({'title': 'Data missing!'}),
            content_type='application/json'
        )

    def test_returns_404_for_non_existent_hearing(self, no_hearing_response):
        assert no_hearing_response.status_code == 404

    def test_returns_400_if_data_is_missing(self, missing_data_response):
        assert missing_data_response.status_code == 400

    def test_returns_missing_fields_in_error_message(
        self, missing_data_response
    ):
        content = missing_data_response.data.decode('utf8')
        assert 'body' in content
        assert 'username' in content
