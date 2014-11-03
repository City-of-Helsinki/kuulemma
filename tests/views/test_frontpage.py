import pytest
from flask import url_for


@pytest.mark.usefixtures('request_ctx')
def test_frontpage_url():
    assert url_for('frontpage.index') == '/'


@pytest.mark.usefixtures('database')
class TestFrontpageIndex(object):
    @pytest.fixture(scope='class')
    def response(self, client):
        return client.get(url_for('frontpage.index'))

    def test_returns_200(self, response):
        assert response.status_code == 200
