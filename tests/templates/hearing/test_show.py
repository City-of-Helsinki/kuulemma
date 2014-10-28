# -*- coding: utf-8 -*-
import pytest
from flask import render_template

from tests.factories import HearingFactory, HearingSectionFactory


@pytest.mark.usefixtures('request_ctx')
class TestShowHearingTemplate(object):
    @pytest.fixture(scope='class')
    def hearing(self):
        main_section = HearingSectionFactory.build(
            lead='Lead for this very important hearing.',
            body='Lorem ipsum...'
        )
        return HearingFactory.build(
            main_section=main_section
        )

    @pytest.fixture(scope='class')
    def content(self, hearing):
        return render_template(
            'hearing/show.html',
            hearing=hearing
        )

    def test_page_title_contains_hearing_title(self, content, hearing):
        partial_title = '<title>{title}'.format(title=hearing.title)
        assert partial_title in content

    def test_renders_hearing_title_in_h1(self, content, hearing):
        h1_title = '<h1>{title}</h1>'.format(title=hearing.title)
        assert h1_title in content

    def test_renders_lead(self, content, hearing):
        assert hearing.lead in content

    def test_renders_body(self, content, hearing):
        assert hearing.body in content
