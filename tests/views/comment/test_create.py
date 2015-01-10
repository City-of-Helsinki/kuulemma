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

from kuulemma.models import Comment
from tests.factories import (
    AlternativeFactory,
    CommentFactory,
    HearingFactory,
    ImageFactory
)


@pytest.fixture
def hearing():
    return HearingFactory(closes_at=date.today() + timedelta(2))


@pytest.mark.usefixtures('request_ctx')
def test_create_url():
    assert (
        url_for('comment.create', hearing_id=1) ==
        '/hearings/1/links/comments'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCreateCommentOnSuccess(object):
    @pytest.fixture
    def comment_data(self, hearing):
        return {
            'title': 'Hello World!',
            'body': 'I really don\'t like this death star idea!',
            'username': 'Luke Skywalker',
            'object_type': 'hearing',
            'object_id': hearing.id
        }

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

    def test_creates_one_new_comment(self, response):
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
class TestCommentingAlternative(object):
    @pytest.fixture
    def alternative(self):
        return AlternativeFactory()

    @pytest.fixture
    def comment_data(self, alternative):
        return {
            'title': 'Hello World!',
            'body': 'I really don\'t like this death star idea!',
            'username': 'Luke Skywalker',
            'object_type': 'alternative',
            'object_id': alternative.id
        }

    @pytest.fixture
    def response(self, client, hearing, comment_data):
        return client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )

    def test_comments_the_right_alternative(self, response, alternative):
        comment = Comment.query.first()
        assert comment.alternative == alternative

    def test_unexisting_alternative_returns_400(
        self, client, hearing, comment_data
    ):
        comment_data['object_id'] = 999
        response = client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        assert response.status_code == 400


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCommentingImage(object):
    @pytest.fixture
    def image(self):
        return ImageFactory()

    @pytest.fixture
    def comment_data(self, image):
        return {
            'title': 'Hello World!',
            'body': 'I really don\'t like this death star idea!',
            'username': 'Luke Skywalker',
            'object_type': 'image',
            'object_id': image.id
        }

    @pytest.fixture
    def response(self, client, hearing, comment_data):
        return client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )

    def test_comments_the_right_image(self, response, image):
        comment = Comment.query.first()
        assert comment.image == image

    def test_unexisting_image_returns_400(
        self, client, hearing, comment_data
    ):
        comment_data['object_id'] = 999
        response = client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        assert response.status_code == 400


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCommentingComment(object):
    @pytest.fixture
    def comment(self):
        return CommentFactory()

    @pytest.fixture
    def comment_data(self, comment):
        return {
            'title': 'Hello World!',
            'body': 'I really don\'t like this death star idea!',
            'username': 'Luke Skywalker',
            'object_type': 'comment',
            'object_id': comment.id
        }

    @pytest.fixture
    def response(self, client, hearing, comment_data):
        return client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )

    def test_comments_the_right_comment(self, response, comment):
        created_comment = Comment.query.all()[-1]
        assert created_comment.comment == comment

    def test_unexisting_comment_returns_400(
        self, client, hearing, comment_data
    ):
        comment_data['object_id'] = 999
        response = client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        assert response.status_code == 400


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCreateCommentOnError(object):
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

    def test_returns_400_if_hearing_has_closed(self, client):
        hearing = HearingFactory(closes_at=date.today() - timedelta(2))
        comment_data = {
            'title': 'Hello World!',
            'body': 'I really don\'t like this death star idea!',
            'username': 'Luke Skywalker',
            'object_type': 'hearing',
            'object_id': hearing.id
        }
        response = client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_returns_missing_fields_in_error_message(
        self, missing_data_response
    ):
        content = missing_data_response.data.decode('utf8')
        assert 'body' in content
        assert 'username' in content

    def test_returns_error_if_required_fields_are_empty_strings(
        self, client, hearing
    ):
        comment_data = {
            'title': '',
            'body': '',
            'username': '',
            'object_type': 'hearing',
            'object_id': hearing.id
        }
        response = client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_returns_error_if_object_type_is_missing(
        self, client, hearing
    ):
        comment_data = {
            'title': 'Title',
            'body': 'Body',
            'username': 'Darth Vader',
            'object_id': hearing.id
        }
        response = client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_unknow_object_type_returns_400(
        self, client, hearing
    ):
        comment_data = {
            'title': 'Title',
            'body': 'Body',
            'username': 'Username',
            'object_type': 'unknown_type-1',
            'object_id': hearing.id
        }
        response = client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )
        assert response.status_code == 400


@pytest.mark.usefixtures('database', 'request_ctx')
class TestCreateCommentHoneyPotSpamFilter(object):
    @pytest.fixture
    def comment_data(self, hearing):
        return {
            'title': 'Hello World!',
            'body': 'I really don\'t like this death star idea!',
            'username': 'Luke Skywalker',
            'object_type': 'hearing',
            'object_id': hearing.id,
            'hp': ''
        }

    @pytest.fixture
    def response(self, client, hearing, comment_data):
        return client.post(
            url_for('comment.create', hearing_id=hearing.id),
            data=json.dumps(comment_data),
            content_type='application/json'
        )

    def test_returns_400(self, response):
        assert response.status_code == 400
