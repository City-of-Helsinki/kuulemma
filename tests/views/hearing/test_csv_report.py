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
import pytest
from flask import url_for

from tests.factories import HearingFactory


@pytest.mark.usefixtures('request_ctx')
def test_csv_report_url():
    assert (
        url_for('hearing.report_as_csv', slug='some-slug') ==
        '/some-slug/raportti.csv'
    )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestHearingCsvReportOnSuccess(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory(published=True)

    @pytest.fixture
    def response(self, client, hearing):
        return client.get(
            url_for('hearing.report_as_csv', slug=hearing.slug)
        )

    def test_returns_200(self, response):
        assert response.status_code == 200

    def test_returns_csv_file(self, response):
        assert response.data.decode('utf8') == (
            '"Otsikko","Viittaa","Kirjoittaja","Saapunut","Kannatettu"'
            ',"Mielipide"\r\n'
        )


@pytest.mark.usefixtures('database', 'request_ctx')
class TestHearingCsvReportOnError(object):
    def test_returns_404_for_non_existent_hearing(self, client):
        response = client.get(
            url_for('hearing.report_as_csv', slug='abcde')
        )
        assert response.status_code == 404

    def test_returns_404_for_unpublished_hearing(self, client):
        hearing = HearingFactory(published=False)
        response = client.get(
            url_for('hearing.show', hearing_id=hearing.id, slug=hearing.slug)
        )
        assert response.status_code == 404
