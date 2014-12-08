import pytest
from flask import url_for

from tests.factories import HearingFactory


@pytest.mark.usefixtures('request_ctx')
def test_report_url():
    assert (
        url_for('hearing.report', slug='some-slug') ==
        '/some-slug/raportti.csv'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestHearingReportOnSuccess(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory(published=True)

    @pytest.fixture
    def response(self, client, hearing):
        return client.get(
            url_for('hearing.report', slug=hearing.slug)
        )

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_returns_csv_file(self, response):
        assert response.data.decode('utf8') == (
            '"Otsikko","Viittaa","Kirjoittaja","Saapunut","Kannatettu"'
            ',"Mielipide"\r\n'
        )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestHearingReportOnError(object):
    def test_returns_404_for_non_existent_hearing(self, client):
        response = client.get(
            url_for('hearing.report', slug='abcde')
        )
        assert response.status_code == 404

    def test_returns_404_for_unpublished_hearing(self, client):
        hearing = HearingFactory(published=False)
        response = client.get(
            url_for('hearing.show', hearing_id=hearing.id, slug=hearing.slug)
        )
        assert response.status_code == 404
