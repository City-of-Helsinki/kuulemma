# -*- coding: utf-8 -*-
import pytest
from inflection import parameterize
from sqlalchemy_continuum.utils import count_versions
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from ..factories import HearingFactory


class TestHearing(object):
    @pytest.fixture(scope='class')
    def hearing(self):
        return HearingFactory.build()

    def test_repr(self, hearing):
        expected = '<Hearing title=\'{title}\'>'.format(title=hearing.title)
        assert repr(hearing) == expected

    def test_uses_parametrized_title_as_slug(self, hearing):
        assert hearing.slug == parameterize(hearing.title)


@pytest.mark.usefixtures('database')
class TestHearingWithDatabase(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.mark.parametrize(
        'column_name',
        [
            'created_at',
            'title',
            'lead',
            'body',
        ]
    )
    def test_non_nullable_columns(self, column_name, hearing):
        assert_non_nullable(hearing, column_name)

    def test_updated_at_is_nullable(self, hearing):
        assert_nullable(hearing, 'updated_at')

    def test_title_max_length_is_255(self, hearing):
        assert_max_length(hearing, 'title', 255)

    def test_uses_versioning(self, hearing):
        assert count_versions(hearing) == 1
