import pytest
from flask import url_for

from tests.factories import HearingFactory
from tests.utils import assert_redirects


@pytest.mark.usefixtures('request_ctx')
def test_hearing_url():
    assert (
        url_for('hearing.show', hearing_id=1, slug='some-slug') ==
        '/kuulemiset/1-some-slug'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestShowHearingWhenHearingExists(object):
    @pytest.fixture(scope='function')
    def hearing(self):
        return HearingFactory()

    @pytest.fixture(scope='function')
    def response(self, client, hearing):
        return client.get(
            url_for('hearing.show', hearing_id=hearing.id, slug=hearing.slug)
        )

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_redirects_to_correct_url_with_wrong_slug(self, client, hearing):
        response = client.get(
            url_for('hearing.show', hearing_id=hearing.id, slug='wrong-slug')
        )
        redirect_url = url_for(
            'hearing.show', hearing_id=hearing.id, slug=hearing.slug
        )
        assert_redirects(response, redirect_url)


@pytest.mark.usefixtures('database', 'request_ctx')
class TestShowHearingWhenHearingDoesNotExist(object):
    @pytest.fixture(scope='class')
    def response(self, client):
        return client.get(
            url_for('hearing.show', hearing_id=999, slug='abcde')
        )

    def test_returns_404_for_non_existent_hearing(self, response):
        assert response.status_code == 404
