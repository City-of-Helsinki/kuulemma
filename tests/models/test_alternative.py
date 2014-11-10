# -*- coding: utf-8 -*-
from datetime import datetime

import pytest
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from ..factories import AlternativeFactory


class TestAlternative(object):
    def test_repr(self):
        alternative = AlternativeFactory.build()
        expected = '<Alternative title=\'{title}\'>'.format(
            title=alternative.title
        )
        assert repr(alternative) == expected


@pytest.mark.usefixtures('database')
class TestAlternativeWithDatabase(object):
    @pytest.fixture
    def alternative(self):
        return AlternativeFactory()

    @pytest.mark.parametrize(
        'column_name',
        [
            'created_at',
            'title',
            'lead',
            'body',
        ]
    )
    def test_non_nullable_columns(self, column_name, alternative):
        assert_non_nullable(alternative, column_name)

    def test_created_at_defaults_to_datetime(self):
        assert isinstance(
            AlternativeFactory(created_at=None).created_at,
            datetime
        )

    def test_updated_at_is_nullable(self, alternative):
        assert_nullable(alternative, 'updated_at')

    def test_updated_at_defaults_to_datetime(self):
        assert isinstance(
            AlternativeFactory(updated_at=None).created_at,
            datetime
        )

    def test_title_max_length_is_255(self, alternative):
        assert_max_length(alternative, 'title', 255)

    def test_title_defaults_to_empty_string(self):
        assert AlternativeFactory(title=None).title == ''

    def test_lead_defaults_to_empty_string(self):
        assert AlternativeFactory(lead=None).lead == ''

    def test_body_defaults_to_empty_string(self):
        assert AlternativeFactory(body=None).body == ''

    def test_hearing_id_is_nullable(self, alternative):
        assert_nullable(alternative, 'hearing_id')
