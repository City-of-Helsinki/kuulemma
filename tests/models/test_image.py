# -*- coding: utf-8 -*-
from datetime import datetime

import pytest
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from ..factories import HearingFactory, ImageFactory


class TestImage(object):
    def test_repr(self):
        image = ImageFactory.build()
        expected = '<Image image_url=\'{image_url}\'>'.format(
            image_url=image.image_url
        )
        assert repr(image) == expected


@pytest.mark.usefixtures('database')
class TestImageWithDatabase(object):
    @pytest.fixture
    def image(self):
        return ImageFactory()

    @pytest.mark.parametrize(
        'column_name',
        [
            'created_at',
            'image_url',
            'caption',
        ]
    )
    def test_non_nullable_columns(self, column_name, image):
        assert_non_nullable(image, column_name)

    def test_created_at_defaults_to_datetime(self):
        assert isinstance(
            ImageFactory(created_at=None).created_at,
            datetime
        )

    def test_updated_at_is_nullable(self, image):
        assert_nullable(image, 'updated_at')

    def test_updated_at_defaults_to_datetime(self):
        assert isinstance(
            ImageFactory(updated_at=None).created_at,
            datetime
        )

    def test_image_url_max_length_is_255(self, image):
        assert_max_length(image, 'image_url', 255)

    def test_image_url_defaults_to_empty_string(self):
        assert ImageFactory(image_url=None).image_url == ''

    def test_caption_defaults_to_empty_string(self):
        assert ImageFactory(caption=None).caption == ''


@pytest.mark.usefixtures('database')
class TestImagePosition(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.fixture
    def image(self, hearing):
        image = ImageFactory()
        hearing.images.append(image)
        return image

    def test_position_should_be_automatically_set(self, image, hearing):
        assert hearing.images[0].position == 0

    def test_position_should_update_automatically(sefl, image, hearing):
        from kuulemma.extensions import db
        assert hearing.images[0].position == 0
        hearing.images.insert(
            0, ImageFactory.build()
        )
        db.session.commit()
        assert hearing.images[1].position == 1
