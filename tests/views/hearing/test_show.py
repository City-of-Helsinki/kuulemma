import pytest
from flask import url_for

from tests.factories import HearingFactory


@pytest.mark.usefixtures('request_ctx')
def test_hearing_url():
    assert url_for('hearing.show', hearing_id=1) == '/kuulemiset/1'


@pytest.mark.usefixtures('database', 'request_ctx')
class TestShowHearingWhenHearingExists(object):
    @pytest.fixture(scope='class')
    def hearing(self):
        return HearingFactory()

    @pytest.fixture(scope='class')
    def response(self, client, hearing):
        return client.get(url_for('hearing.show', hearing_id=hearing.id))

    def test_returns_200(self, response):
        assert response.status_code == 200


@pytest.mark.usefixtures('database', 'request_ctx')
class TestShowHearingWhenHearingDoesNotExist(object):
    @pytest.fixture(scope='class')
    def response(self, client):
        return client.get(url_for('hearing.show', hearing_id=999))

    def test_returns_404_for_non_existent_hearing(self, response):
        assert response.status_code == 404
