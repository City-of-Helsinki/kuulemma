# -*- coding: utf-8 -*-
from datetime import datetime

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
    @pytest.fixture
    def hearing_section(self):
        return HearingSectionFactory()

    @pytest.mark.parametrize(
        'column_name',
        [
            'created_at',
            'title',
            'lead',
            'body',
        ]
    )
    def test_non_nullable_columns(self, column_name, hearing_section):
        assert_non_nullable(hearing_section, column_name)

    def test_created_at_defaults_to_datetime(self):
        assert isinstance(
            HearingSectionFactory(created_at=None).created_at,
            datetime
        )

    def test_updated_at_is_nullable(self, hearing_section):
        assert_nullable(hearing_section, 'updated_at')

    def test_updated_at_defaults_to_datetime(self):
        assert isinstance(
            HearingSectionFactory(updated_at=None).created_at,
            datetime
        )

    def test_title_max_length_is_255(self, hearing_section):
        assert_max_length(hearing_section, 'title', 255)

    def test_title_defaults_to_empty_string(self):
        assert HearingSectionFactory(title=None).title == ''

    def test_lead_defaults_to_empty_string(self):
        assert HearingSectionFactory(lead=None).lead == ''

    def test_body_defaults_to_empty_string(self):
        assert HearingSectionFactory(body=None).body == ''

    def test_hearing_id_is_nullable(self, hearing_section):
        assert_nullable(hearing_section, 'hearing_id')
