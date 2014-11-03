# -*- coding: utf-8 -*-
from datetime import datetime

import pytest
from sqlalchemy_continuum.utils import count_versions
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from ..factories import CommentFactory, LikeFactory


class TestComment(object):
    @pytest.fixture(scope='class')
    def comment(self):
        return CommentFactory.build()

    def test_repr(self, comment):
        expected = '<Comment title=\'{title}\'>'.format(
            title=comment.title
        )
        assert repr(comment) == expected

    def test_like_count(self, comment):
        expected = 2
        for _ in range(expected):
            comment.likes.append(LikeFactory.build())
        assert comment.like_count == expected


@pytest.mark.usefixtures('database')
class TestCommentWithDatabase(object):
    @pytest.fixture
    def comment(self):
        return CommentFactory()

    @pytest.mark.parametrize(
        'column_name',
        [
            'created_at',
            'title',
            'lead',
            'body',
            'username',
        ]
    )
    def test_non_nullable_columns(self, column_name, comment):
        assert_non_nullable(comment, column_name)

    def test_created_at_defaults_to_datetime(self):
        assert isinstance(CommentFactory(created_at=None).created_at, datetime)

    def test_updated_at_is_nullable(self, comment):
        assert_nullable(comment, 'updated_at')

    def test_updated_at_defaults_to_datetime(self):
        assert isinstance(CommentFactory(updated_at=None).created_at, datetime)

    def test_title_max_length_is_255(self, comment):
        assert_max_length(comment, 'title', 255)

    def test_title_defaults_to_empty_string(self):
        assert CommentFactory(title=None).title == ''

    def test_lead_defaults_to_empty_string(self):
        assert CommentFactory(lead=None).lead == ''

    def test_body_defaults_to_empty_string(self):
        assert CommentFactory(body=None).body == ''

    def test_username_max_length_is_255(self, comment):
        assert_max_length(comment, 'username', 255)

    def test_username_defaults_to_empty_string(self):
        assert CommentFactory(username=None).username == ''

    def test_uses_versioning(self, comment):
        assert count_versions(comment) == 1
