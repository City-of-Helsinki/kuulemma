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

from datetime import datetime

import pytest
from sqlalchemy_utils import assert_non_nullable, assert_nullable

from ..factories import FeedbackFactory


class TestFeedback(object):
    def test_repr(self):
        feedback = FeedbackFactory.build()
        expected = '<Feedback content=\'{content}\'>'.format(
            content=feedback.content
        )
        assert repr(feedback) == expected


@pytest.mark.usefixtures('database')
class TestFeedbackWithDatabase(object):
    @pytest.fixture
    def feedback(self):
        return FeedbackFactory()

    @pytest.mark.parametrize(
        'column_name',
        [
            'created_at',
            'content',
        ]
    )
    def test_non_nullable_columns(self, column_name, feedback):
        assert_non_nullable(feedback, column_name)

    def test_created_at_defaults_to_datetime(self):
        assert isinstance(
            FeedbackFactory(created_at=None).created_at,
            datetime
        )

    def test_updated_at_is_nullable(self, feedback):
        assert_nullable(feedback, 'updated_at')

    def test_content_defaults_to_empty_string(self):
        assert FeedbackFactory(content=None).content == ''
