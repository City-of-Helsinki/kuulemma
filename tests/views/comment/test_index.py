import json

import pytest
from flask import url_for

from tests.factories import (
    AlternativeFactory,
    CommentFactory,
    HearingFactory,
    ImageFactory,
    UserFactory
)
from tests.utils import login_user


@pytest.mark.usefixtures('request_ctx')
def test_index_url():
    assert (
        url_for('comment.index', hearing_id=1) ==
        '/hearings/1/links/comments'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestIndexOnSuccess(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory()

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

    def test_returns_comments_ordered_desc_by_created_at(
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
class TestIndexOnError(object):
    @pytest.fixture
    def response(self, client):
        return client.get(
            url_for('comment.index', hearing_id=999)
        )

    def test_returns_404_if_hearing_does_not_exist(self, response):
        assert response.status_code == 404
