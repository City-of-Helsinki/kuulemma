import json

import pytest
from flask import url_for

from kuulemma.models import Feedback
from tests.factories import FeedbackFactory


@pytest.mark.usefixtures('request_ctx')
def test_create_feedback_url():
    assert (
        url_for('feedback.create') == '/feedback'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCreateFeedbackOnSuccess(object):
    @pytest.fixture
    def feedback_data(self):
        return {'content': 'This is feedback!'}

    @pytest.fixture
    def response(self, client, feedback_data):
        return client.post(
            url_for('feedback.create'),
            data=json.dumps(feedback_data),
            content_type='application/json'
        )

    def test_returns_201(self, response):
        assert response.status_code == 201

    def test_returns_the_created_feedbacks(self, response, feedback_data):
        content = response.data.decode('utf8')
        assert feedback_data['content'] in content

    def test_creates_a_new_feedback(self, response):
        assert Feedback.query.count() == 1

    def test_saves_feedback_content(self, response, feedback_data):
        feedback = Feedback.query.first()
        assert feedback.content == feedback_data['content']


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCreateFeedbackOnError(object):
    @pytest.fixture
    def response(self, client, user, comment):
        FeedbackFactory(user=user, comment=comment)
        return client.post(
            url_for('feedback.create', user_id=user.id),
            data=json.dumps({'comment_id': comment.id}),
            content_type='application/json'
        )

    def test_returns_400_if_json_is_missing(self, client):
        response = client.post(
            url_for('feedback.create')
        )
        assert response.status_code == 400

    def test_returns_400_if_content_is_missing(self, client):
        response = client.post(
            url_for('feedback.create'),
            data=json.dumps({'other_data': 'info'}),
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_returns_400_if_content_is_empty_string(self, client):
        response = client.post(
            url_for('feedback.create'),
            data=json.dumps({'content': ''}),
            content_type='application/json'
        )
        assert response.status_code == 400
