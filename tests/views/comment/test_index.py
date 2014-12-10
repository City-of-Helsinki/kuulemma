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

from tests.factories import (
    AlternativeFactory,
    CommentFactory,
    HearingFactory,
    ImageFactory,
    LikeFactory,
    UserFactory
)
from tests.utils import login_user


@pytest.mark.usefixtures('request_ctx')
def test_index_url():
    assert (
        url_for('comment.index', hearing_id=1) ==
        '/hearings/1/links/comments'
    )


@pytest.fixture
def hearing():
    return HearingFactory()


@pytest.mark.usefixtures('database', 'request_ctx')
class TestIndexOnSuccessWithoutParameters(object):
    @pytest.fixture
    def comments(self, hearing):
        return [
            CommentFactory(hearing=hearing),
            CommentFactory(hearing=hearing)
        ]

    @pytest.fixture
    def response(self, client, hearing, comments):
        return client.get(
            url_for('comment.index', hearing_id=hearing.id)
        )

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_returns_empty_list_if_there_are_no_comments(
        self, client, hearing
    ):
        response = client.get(
            url_for('comment.index', hearing_id=hearing.id)
        )
        content = response.data.decode('utf8')
        assert '"comments": []' in content

    def test_returns_list_of_comments(self, response, comments):
        content = response.data.decode('utf8')
        assert comments[0].title in content
        assert comments[1].title in content

    def test_returns_comments_ordered_by_desc_created_at(
        self, client, hearing
    ):
        image = ImageFactory()
        alternative = AlternativeFactory(main_image=image)
        hearing.alternatives.append(alternative)

        first_comment = CommentFactory(hearing=None, alternative=alternative)
        second_comment = CommentFactory(hearing=None, image=image)
        third_comment = CommentFactory(hearing=hearing)

        response = client.get(
            url_for('comment.index', hearing_id=hearing.id)
        )
        comments = json.loads(response.data.decode('utf8'))['comments']

        assert comments[0]['id'] == third_comment.id
        assert comments[1]['id'] == second_comment.id
        assert comments[2]['id'] == first_comment.id

    def test_does_not_return_hidden_comments_to_non_officials(
        self, client, hearing
    ):
        CommentFactory(hearing=hearing, is_hidden=True)
        response = client.get(
            url_for('comment.index', hearing_id=hearing.id)
        )
        content = response.data.decode('utf8')
        assert '"comments": []' in content

    def test_returns_hidden_comments_to_officials(self, client, hearing):
        user = UserFactory(is_official=True)
        login_user(client, user)
        comment = CommentFactory(hearing=hearing, is_hidden=True)
        response = client.get(
            url_for('comment.index', hearing_id=hearing.id)
        )
        content = response.data.decode('utf8')
        assert comment.title in content


@pytest.mark.usefixtures('database', 'request_ctx')
class TestIndexOnSuccessWithParameters(object):
    @pytest.fixture
    def comments(self, hearing):
        return [
            CommentFactory(hearing=hearing),
            CommentFactory(hearing=hearing),
            CommentFactory(hearing=hearing)
        ]

    def test_uses_per_page_to_define_number_of_comments(
        self, client, hearing, comments
    ):
        per_page = 1
        response = client.get(
            url_for('comment.index', hearing_id=hearing.id, per_page=per_page)
        )
        comments = json.loads(response.data.decode('utf8'))['comments']
        assert len(comments) == per_page

    def test_uses_page_to_define_which_page_to_return(
        self, client, hearing, comments
    ):
        response = client.get(
            url_for(
                'comment.index',
                hearing_id=hearing.id,
                per_page=1,
                page=2
            )
        )
        paginated = json.loads(response.data.decode('utf8'))['comments']

        assert len(paginated) == 1
        assert comments[1].id == paginated[0]['id']

    def test_returns_comments_ordered_by_like_count_with_order_by_like_count(
        self, client, hearing, comments
    ):
        LikeFactory(comment=comments[0])
        LikeFactory(comment=comments[0])
        LikeFactory(comment=comments[1])
        LikeFactory(comment=comments[1])
        LikeFactory(comment=comments[1])
        LikeFactory(comment=comments[2])

        response = client.get(
            url_for(
                'comment.index', hearing_id=hearing.id, order_by='like_count'
            )
        )
        paginated = json.loads(response.data.decode('utf8'))['comments']

        assert paginated[0]['id'] == comments[1].id
        assert paginated[1]['id'] == comments[0].id
        assert paginated[2]['id'] == comments[2].id

    def test_order_by_like_count_returns_only_liked_comments(
        self, client, hearing, comments
    ):
        LikeFactory(comment=comments[0])

        response = client.get(
            url_for(
                'comment.index', hearing_id=hearing.id, order_by='like_count'
            )
        )
        content = response.data.decode('utf8')

        assert comments[0].title in content
        assert comments[1].title not in content
        assert comments[2].title not in content


@pytest.mark.usefixtures('database', 'request_ctx')
class TestIndexOnError(object):
    @pytest.fixture
    def response(self, client):
        return client.get(
            url_for('comment.index', hearing_id=999)
        )

    def test_returns_404_if_hearing_does_not_exist(self, response):
        assert response.status_code == 404
