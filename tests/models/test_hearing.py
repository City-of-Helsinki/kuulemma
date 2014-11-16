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

from ..factories import (
    AlternativeFactory,
    CommentFactory,
    HearingFactory,
    ImageFactory
)


class TestHearing(object):
    @pytest.fixture(scope='class')
    def hearing(self):
        return HearingFactory.build()

    def test_repr(self, hearing):
        expected = '<Hearing title=\'{title}\'>'.format(title=hearing.title)
        assert repr(hearing) == expected

    def test_uses_parametrized_title_as_slug(self, hearing):
        assert hearing.slug == parameterize(hearing.title)

    def test_commentable_id(self, hearing):
        expected = 'hearing-{id}'.format(id=hearing.id)
        assert hearing.commentable_id == expected

    def test_commentable_name(self, hearing):
        expected = 'Koko kuuleminen'
        assert hearing.commentable_name == expected

    def test_commentable_option(self, hearing):
        expected = '{id}:{name}'.format(
            id=hearing.commentable_id,
            name=hearing.commentable_name
        )
        assert hearing.commentable_option == expected


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


@pytest.mark.usefixtures('database')
class TestAllCommentsProperty(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory()

    @pytest.fixture
    def other_hearing(self):
        return HearingFactory()

    @pytest.fixture
    def alternative(self):
        return AlternativeFactory()

    @pytest.fixture
    def image(self):
        return ImageFactory()

    def test_without_comments(self, hearing):
        assert hearing.all_comments.all() == []

    def test_hearing_comment(self, hearing):
        comment = CommentFactory(hearing=hearing)
        assert hearing.all_comments.all() == [comment]

    def test_hearing_main_image_comment(self, hearing, image):
        hearing.main_image = image
        comment = CommentFactory(image=image, hearing=None)
        assert hearing.all_comments.all() == [comment]

    def test_hearing_image_comment(self, hearing, image):
        hearing.images.append(image)
        comment = CommentFactory(hearing=None, image=image)
        assert hearing.all_comments.all() == [comment]

    def test_alternative_comment(self, hearing, alternative):
        hearing.alternatives.append(alternative)
        comment = CommentFactory(hearing=None, alternative=alternative)
        assert hearing.all_comments.all() == [comment]

    def test_alternative_main_image_comment(self, hearing, alternative, image):
        alternative.main_image = image
        hearing.alternatives.append(alternative)
        comment = CommentFactory(hearing=None, alternative=alternative)
        assert hearing.all_comments.all() == [comment]

    def test_alternative_image_comment(self, hearing, alternative, image):
        alternative.images.append(image)
        hearing.alternatives.append(alternative)
        comment = CommentFactory(hearing=None, alternative=alternative)
        assert hearing.all_comments.all() == [comment]

    # Comments commenting other comment tests
    # ---------------------------------------

    def test_hearing_comment_comment(self, hearing):
        parent = CommentFactory(hearing=hearing)
        comment = CommentFactory(hearing=None, comment=parent)
        assert comment in hearing.all_comments.all()

    def test_hearing_main_image_comment_comment(self, hearing, image):
        hearing.main_image = image
        parent = CommentFactory(image=image, hearing=None)
        comment = CommentFactory(hearing=None, comment=parent)
        assert comment in hearing.all_comments.all()

    def test_hearing_image_comment_comment(self, hearing, image):
        hearing.images.append(image)
        parent = CommentFactory(hearing=None, image=image)
        comment = CommentFactory(hearing=None, comment=parent)
        assert comment in hearing.all_comments.all()

    def test_alternative_comment_comment(self, hearing, alternative):
        hearing.alternatives.append(alternative)
        parent = CommentFactory(hearing=None, alternative=alternative)
        comment = CommentFactory(hearing=None, comment=parent)
        assert comment in hearing.all_comments.all()

    def test_alternative_main_image_comment_comment(
        self, hearing, alternative, image
    ):
        alternative.main_image = image
        hearing.alternatives.append(alternative)
        parent = CommentFactory(hearing=None, alternative=alternative)
        comment = CommentFactory(hearing=None, comment=parent)
        assert comment in hearing.all_comments.all()

    def test_alternative_image_comment_comment(
        self, hearing, alternative, image
    ):
        alternative.images.append(image)
        hearing.alternatives.append(alternative)
        parent = CommentFactory(hearing=None, alternative=alternative)
        comment = CommentFactory(hearing=None, comment=parent)
        assert comment in hearing.all_comments.all()

    # Comments in other hearings
    # --------------------------

    def test_other_hearing_comment(self, hearing, other_hearing):
        comment = CommentFactory(hearing=other_hearing)
        assert comment not in hearing.all_comments.all()

    def test_other_hearing_main_image_comment(
        self, hearing, other_hearing, image
    ):
        other_hearing.main_image = image
        comment = CommentFactory(image=image, hearing=None)
        assert comment not in hearing.all_comments.all()

    def test_other_hearing_image_comment(self, hearing, other_hearing, image):
        other_hearing.images.append(image)
        comment = CommentFactory(hearing=None, image=image)
        assert comment not in hearing.all_comments.all()

    def test_other_alternative_comment(
        self, hearing, other_hearing, alternative
    ):
        other_hearing.alternatives.append(alternative)
        comment = CommentFactory(hearing=None, alternative=alternative)
        assert comment not in hearing.all_comments.all()

    def test_other_alternative_main_image_comment(
        self, hearing, other_hearing, alternative, image
    ):
        alternative.main_image = image
        other_hearing.alternatives.append(alternative)
        comment = CommentFactory(hearing=None, alternative=alternative)
        assert comment not in hearing.all_comments.all()

    def test_other_alternative_image_comment(
        self, hearing, other_hearing, alternative, image
    ):
        alternative.images.append(image)
        other_hearing.alternatives.append(alternative)
        comment = CommentFactory(hearing=None, alternative=alternative)
        assert comment not in hearing.all_comments.all()


@pytest.mark.usefixtures('database')
class TestGetCommentableSectionsString(object):
    @pytest.fixture
    def image(self):
        return ImageFactory()

    @pytest.fixture
    def images(self):
        return [
            ImageFactory(),
            ImageFactory()
        ]

    @pytest.fixture
    def alternatives(self):
        return [
            AlternativeFactory(),
            AlternativeFactory()
        ]

    @pytest.fixture
    def hearing(self, alternatives):
        return HearingFactory()

    def test_contains_own_data(self, hearing):
        assert (
            hearing.commentable_id in
            hearing.get_commentable_sections_string()
        )

    def test_contains_main_image(self, hearing, image):
        hearing.main_image = image
        assert (
            image.commentable_id in hearing.get_commentable_sections_string()
        )

    def test_contains_data_of_all_the_images(self, hearing, images):
        hearing.images = images
        content = hearing.get_commentable_sections_string()
        assert images[0].commentable_id in content
        assert images[1].commentable_id in content

    def test_contains_all_the_alternatives(self, hearing, alternatives):
        hearing.alternatives = alternatives
        content = hearing.get_commentable_sections_string()
        assert alternatives[0].commentable_id in content
        assert alternatives[1].commentable_id in content

    def test_data_is_separated_with_semi_colon(self, hearing, image):
        hearing.main_image = image
        content = hearing.get_commentable_sections_string()
        assert len(content.split(';')) == 2
