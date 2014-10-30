import pytest
from flask import url_for

from tests.factories import CommentFactory, HearingFactory


@pytest.mark.usefixtures('request_ctx')
def test_create_url():
    assert (
        url_for('comment.index', hearing_id=1) ==
        '/kuulemiset/1/links/comments'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestIndex(object):
    @pytest.fixture()
    def hearing(self):
        return HearingFactory()

    @pytest.fixture()
    def comments(self, hearing):
        return [
            CommentFactory(hearing=hearing),
            CommentFactory(hearing=hearing)
        ]

    @pytest.fixture()
    def response(self, client, hearing, comments):
        return client.get(
            url_for('comment.index', hearing_id=hearing.id)
        )

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_returns_empty_list_if_there_are_no_comments(self, client):
        response = client.get(url_for('comment.index', hearing_id=999))
        content = response.data.decode('utf8')
        assert '"comments": []' in content

    def test_returns_list_of_comments(self, response, comments):
        content = response.data.decode('utf8')
        assert comments[0].title in content
        assert comments[1].title in content
