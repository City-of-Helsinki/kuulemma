# -*- coding: utf-8 -*-
from datetime import datetime

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from kuulemma.extensions import db

from ..factories import HearingFactory, ImageFactory


class TestImage(object):
    @pytest.fixture
    def image(self):
        return ImageFactory.build(id=1)

    def test_repr(self, image):
        expected = '<Image image_url=\'{image_url}\'>'.format(
            image_url=image.image_url
        )
        assert repr(image) == expected

    def test_commentable_id(self, image):
        assert image.commentable_id == 'image-{id}'.format(id=image.id)

    def test_commentable_name(self, image):
        assert (
            image.commentable_name ==
            'Kuva {number}'.format(number=image.number)
        )

    def test_get_commentable_option(self, image):
        context = 'Koko kuuleminen'
        expected = '{id}:{context} {name}'.format(
            id=image.commentable_id,
            context=context,
            name=image.commentable_name
        )
        assert image.get_commentable_option(context) == expected


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
class TestImageCheckConstraint(object):
    def test_position_must_be_none_if_hearing_and_alternative_id_are_none(
        self
    ):
        with pytest.raises(IntegrityError):
            ImageFactory(
                hearing_id=None,
                alternative_id=None,
                position=1
            )

    def test_position_should_be_gte_0_if_hearing_is_defined(self):
        with pytest.raises(IntegrityError):
            ImageFactory(
                hearing_id=1,
                position=-1
            )

    def test_position_should_be_gte_0_if_hearing_section_is_defined(self):
        with pytest.raises(IntegrityError):
            ImageFactory(
                alternative_id=1,
                position=-1
            )


@pytest.mark.usefixtures('database')
class TestIsMainImage(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.fixture
    def image(self):
        return ImageFactory()

    def test_returns_true_for_main_images(self, image, hearing):
        hearing.main_image = image
        assert image.is_main_image

    def test_returns_false_if_is_regular_image(self, image, hearing):
        hearing.images.append(image)
        # is_main_image works for non main images only after db.flush.
        db.session.flush()
        assert not image.is_main_image


@pytest.mark.usefixtures('database')
class TestImagePositionAndNumber(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.fixture
    def image(self):
        return ImageFactory.build()

    def test_position_should_be_automatically_set(self, hearing):
        hearing.images.append(ImageFactory.build())
        hearing.images.append(ImageFactory.build())
        assert hearing.images[1].position == 1

    def test_position_should_update_automatically(sefl, hearing, image):
        hearing.images.append(image)
        assert image.position == 0
        hearing.images.insert(
            0, ImageFactory.build()
        )
        assert image.position == 1

    def test_main_image_number_should_be_1(self, hearing, image):
        hearing.main_image = image
        assert image.number == 1

    def test_regular_image_numbering_should_start_from_2(self, hearing, image):
        hearing.images.append(image)
        # is_main_image works for non main images only after db.flush.
        db.session.flush()
        assert not image.is_main_image
        assert image.position == 0
        assert image.number == 2
