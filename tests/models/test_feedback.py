# -*- coding: utf-8 -*-
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
