import pytest
from flask import url_for

from tests.asserts.views import assert_redirects
from tests.factories import HearingFactory, UserFactory
from tests.utils import login_user


@pytest.mark.usefixtures('request_ctx')
def test_hearing_url():
    assert (
        url_for('hearing.show', hearing_id=1, slug='some-slug') ==
        '/kuulemiset/1-some-slug'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestShowHearingOnSuccess(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory(published=True)

    @pytest.fixture
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

    def test_returns_unpublished_hearing_to_official(self, client):
        user = UserFactory(is_official=True)
        login_user(client, user)
        hearing = HearingFactory(published=False)
        response = client.get(
            url_for('hearing.show', hearing_id=hearing.id, slug=hearing.slug)
        )
        assert response.status_code == 200


@pytest.mark.usefixtures('database', 'request_ctx')
class TestShowHearingOnError(object):
    @pytest.fixture(scope='class')
    def response(self, client):
        return client.get(
            url_for('hearing.show', hearing_id=999, slug='abcde')
        )

    def test_returns_404_for_non_existent_hearing(self, response):
        assert response.status_code == 404

    def test_returns_404_for_unpublished_hearing(self, client):
        hearing = HearingFactory(published=False)
        response = client.get(
            url_for('hearing.show', hearing_id=hearing.id, slug=hearing.slug)
        )
        assert response.status_code == 404
