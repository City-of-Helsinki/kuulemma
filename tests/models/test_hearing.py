# -*- coding: utf-8 -*-
import pytest
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from ..factories import HearingFactory


class TestHearing(object):
    def test_repr(self):
        hearing = HearingFactory.build()
        expected = '<Hearing title=\'{title}\'>'.format(title=hearing.title)
        assert repr(hearing) == expected


@pytest.mark.usefixtures('database')
class TestHearingWithDatabase(object):
    @pytest.fixture(scope='function')
    def hearing(self):
        return HearingFactory()

    def test_created_at_is_non_nullable(self, hearing):
        assert_non_nullable(hearing, 'created_at')

    def test_updated_at_is_nullable(self, hearing):
        assert_nullable(hearing, 'updated_at')

    def test_title_is_non_nullable(self, hearing):
        assert_non_nullable(hearing, 'title')

    def test_title_max_length_is_255(self, hearing):
        assert_max_length(hearing, 'title', 255)

    def test_lead_is_non_nullable(self, hearing):
        assert_non_nullable(hearing, 'lead')

    def test_body_is_non_nullable(self, hearing):
        assert_non_nullable(hearing, 'body')
