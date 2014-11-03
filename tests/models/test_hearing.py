# -*- coding: utf-8 -*-
from datetime import date, datetime, timedelta

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


class TestDaysOpenProperty(object):
    def test_should_return_number_of_days_the_hearing_is_still_open(self):
        expected = 5
        closes_at = date.today() + timedelta(days=expected)
        hearing = HearingFactory.build(closes_at=closes_at)
        assert hearing.days_open == expected

    def test_should_return_zero_if_closing_date_has_passed(self):
        closes_at = date.today() - timedelta(days=4)
        hearing = HearingFactory.build(closes_at=closes_at)
        assert hearing.days_open == 0

    def test_should_return_zero_if_closing_date_is_none(self):
        hearing = HearingFactory.build()
        assert hearing.days_open == 0


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
            'published'
        ]
    )
    def test_non_nullable_columns(self, column_name, hearing):
        assert_non_nullable(hearing, column_name)

    def test_created_at_defaults_to_datetime(self):
        assert isinstance(HearingFactory(created_at=None).created_at, datetime)

    def test_updated_at_is_nullable(self, hearing):
        assert_nullable(hearing, 'updated_at')

    def test_updated_at_defaults_to_datetime(self):
        assert isinstance(HearingFactory(updated_at=None).created_at, datetime)

    def test_title_max_length_is_255(self, hearing):
        assert_max_length(hearing, 'title', 255)

    def test_title_defaults_to_empty_string(self):
        assert HearingFactory(title=None).title == ''

    def test_lead_defaults_to_empty_string(self):
        assert HearingFactory(lead=None).lead == ''

    def test_body_defaults_to_empty_string(self):
        assert HearingFactory(body=None).body == ''

    def test_opens_at_is_nullable(self, hearing):
        assert_nullable(hearing, 'opens_at')

    def test_opens_at_defaults_to_none(self):
        assert HearingFactory(opens_at=None).opens_at is None

    def test_closes_at_is_nullable(self, hearing):
        assert_nullable(hearing, 'closes_at')

    def test_closes_at_defaults_to_none(self):
        assert HearingFactory(closes_at=None).closes_at is None

    def test_published_defaults_to_false(self):
        assert HearingFactory(published=None).published is False

    def test_uses_versioning(self, hearing):
        assert count_versions(hearing) == 1
