# -*- coding: utf-8 -*-
import pytest
from inflection import parameterize
from sqlalchemy_continuum.utils import count_versions
from sqlalchemy_utils import assert_non_nullable, assert_nullable

from ..factories import HearingFactory


class TestHearing(object):
    @pytest.fixture(scope='function')
    def hearing(self):
        return HearingFactory.build()

    def test_repr(self, hearing):
        expected = '<Hearing title=\'{title}\'>'.format(title=hearing.title)
        assert repr(hearing) == expected

    def test_title_uses_main_section_title(self, hearing):
        assert hearing.title == hearing.main_section.title

    def test_lead_uses_main_section_lead(self, hearing):
        assert hearing.lead == hearing.main_section.lead

    def test_body_uses_main_section_body(self, hearing):
        assert hearing.body == hearing.main_section.body

    def test_uses_parametrized_main_section_title_as_slug(self, hearing):
        assert hearing.slug == parameterize(hearing.main_section.title)


@pytest.mark.usefixtures('database')
class TestHearingWithDatabase(object):
    @pytest.fixture(scope='function')
    def hearing(self):
        return HearingFactory()

    def test_created_at_is_non_nullable(self, hearing):
        assert_non_nullable(hearing, 'created_at')

    def test_updated_at_is_nullable(self, hearing):
        assert_nullable(hearing, 'updated_at')

    def test_uses_versioning(self, hearing):
        assert count_versions(hearing) == 1
