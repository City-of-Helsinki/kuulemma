# -*- coding: utf-8 -*-
import pytest
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from ..factories import HearingSectionFactory


class TestHearingSection(object):
    def test_repr(self):
        hearing_section = HearingSectionFactory.build()
        expected = '<HearingSection title=\'{title}\'>'.format(
            title=hearing_section.title
        )
        assert repr(hearing_section) == expected


@pytest.mark.usefixtures('database')
class TestHearingSectionWithDatabase(object):
    @pytest.fixture(scope='function')
    def hearing_section(self):
        return HearingSectionFactory()

    def test_created_at_is_non_nullable(self, hearing_section):
        assert_non_nullable(hearing_section, 'created_at')

    def test_updated_at_is_nullable(self, hearing_section):
        assert_nullable(hearing_section, 'updated_at')

    def test_title_is_non_nullable(self, hearing_section):
        assert_non_nullable(hearing_section, 'title')

    def test_title_max_length_is_255(self, hearing_section):
        assert_max_length(hearing_section, 'title', 255)

    def test_lead_is_non_nullable(self, hearing_section):
        assert_non_nullable(hearing_section, 'lead')

    def test_body_is_non_nullable(self, hearing_section):
        assert_non_nullable(hearing_section, 'body')

    def test_hearing_id_is_nullable(self, hearing_section):
        assert_nullable(hearing_section, 'hearing_id')
