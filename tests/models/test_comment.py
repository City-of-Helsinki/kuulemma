# -*- coding: utf-8 -*-
import pytest
from sqlalchemy_continuum.utils import count_versions
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from ..factories import CommentFactory


class TestComment(object):
    def test_repr(self):
        comment = CommentFactory.build()
        expected = '<Comment title=\'{title}\'>'.format(
            title=comment.title
        )
        assert repr(comment) == expected


@pytest.mark.usefixtures('database')
class TestCommentWithDatabase(object):
    @pytest.fixture(scope='function')
    def comment(self):
        return CommentFactory()

    def test_created_at_is_non_nullable(self, comment):
        assert_non_nullable(comment, 'created_at')

    def test_updated_at_is_nullable(self, comment):
        assert_nullable(comment, 'updated_at')

    def test_title_is_non_nullable(self, comment):
        assert_non_nullable(comment, 'title')

    def test_title_max_length_is_255(self, comment):
        assert_max_length(comment, 'title', 255)

    def test_lead_is_non_nullable(self, comment):
        assert_non_nullable(comment, 'lead')

    def test_body_is_non_nullable(self, comment):
        assert_non_nullable(comment, 'body')

    def test_username_is_non_nullable(self, comment):
        assert_non_nullable(comment, 'username')

    def test_username_max_length_is_255(self, comment):
        assert_max_length(comment, 'username', 255)

    def test_uses_versioning(self, comment):
        assert count_versions(comment) == 1
