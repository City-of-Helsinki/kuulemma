# -*- coding: utf-8 -*-
# Kuulemma
# Copyright (C) 2014, Fast Monkeys Oy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest
from flask import render_template
from flexmock import flexmock

from tests.factories import AlternativeFactory, HearingFactory, ImageFactory


@pytest.mark.usefixtures('request_ctx')
class ShowHearingTemplateTestCase(object):
    @pytest.fixture(scope='class')
    def content(self, hearing):
        (
            flexmock(hearing)
            .should_receive('comment_count')
            .and_return(2)
        )
        return render_template(
            'hearing/show.html',
            hearing=hearing
        )


class TestMainContent(ShowHearingTemplateTestCase):
    @pytest.fixture(scope='class')
    def main_image(self):
        return ImageFactory.build(
            filename='main/image/url.jpg',
            caption='Main image caption'
        )

    @pytest.fixture(scope='class')
    def images(self):
        return [
            ImageFactory.build(
                filename='regular/image/url.jpg',
                caption='Regular image caption'
            ),
            ImageFactory.build(
                filename='another/image/url.jpg',
                caption='Another image caption'
            )
        ]

    @pytest.fixture(scope='class')
    def hearing(self, main_image, images):
        return HearingFactory.build(
            lead='Lead for this very important hearing.',
            body='Lorem ipsum...',
            main_image=main_image,
            images=images
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

    def test_renders_main_image(self, content, hearing, main_image):
        assert main_image.filename in content

    def test_renders_main_image_caption(self, content, hearing, main_image):
        assert main_image.caption in content

    def test_renders_all_regular_images(self, content, hearing, images):
        assert images[0].filename in content
        assert images[1].filename in content

    def test_renders_captions_for_all_regular_images(
        self, content, hearing, images
    ):
        assert images[0].caption in content
        assert images[1].caption in content


class TestAlternatives(ShowHearingTemplateTestCase):
    @pytest.fixture(scope='class')
    def main_image(self):
        return ImageFactory.build(
            filename='main/image/url.jpg',
            caption='Main image caption'
        )

    @pytest.fixture(scope='class')
    def images(self):
        return [
            ImageFactory.build(
                filename='regular/image/url.jpg',
                caption='Regular image caption'
            ),
            ImageFactory.build(
                filename='another/image/url.jpg',
                caption='Another image caption'
            )
        ]

    @pytest.fixture(scope='class')
    def alternative(self, main_image, images):
        return AlternativeFactory.build(
            title='Alternative A',
            lead='Lorem ipsum...',
            body='Alternative lead',
            main_image=main_image,
            images=images
        )

    @pytest.fixture(scope='class')
    def hearing(self, alternative):
        return HearingFactory.build(
            lead='Lead for this very important hearing.',
            body='Lorem ipsum...',
            alternatives=[alternative]
        )

    def test_renders_alternatives_title(self, content, alternative):
        assert alternative.title in content

    def test_renders_alternatives_lead(self, content, alternative):
        assert alternative.lead in content

    def test_renders_alternatives_body(self, content, alternative):
        assert alternative.body in content

    def test_renders_main_image(self, content, hearing, main_image):
        assert main_image.filename in content

    def test_renders_all_regular_images(self, content, hearing, images):
        assert images[0].filename in content
        assert images[1].filename in content

    def test_renders_captions_for_all_regular_images(
        self, content, hearing, images
    ):
        assert images[0].caption in content
        assert images[1].caption in content
