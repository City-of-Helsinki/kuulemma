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
