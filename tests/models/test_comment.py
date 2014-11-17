# -*- coding: utf-8 -*-
from datetime import datetime

import pytest
from sqlalchemy.exc import IntegrityError
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
    ImageFactory,
    LikeFactory
)


class TestComment(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory.build()

    @pytest.fixture
    def alternative(self):
        return AlternativeFactory.build()

    @pytest.fixture
    def image(self):
        return ImageFactory.build()

    @pytest.fixture
    def comment(self):
        return CommentFactory.build()

    def test_repr(self, comment):
        expected = '<Comment title=\'{title}\'>'.format(
            title=comment.title
        )
        assert repr(comment) == expected

    def test_like_count(self, comment):
        expected = 2
        for _ in range(expected):
            comment.likes.append(LikeFactory.build())
        assert comment.like_count == expected

    def test_tag_when_comments_hearing(self, hearing, comment):
        comment.hearing = hearing
        assert comment.tag == ''

    def test_tag_when_comments_alternative(self, alternative, comment):
        comment.alternative = alternative
        assert comment.tag == alternative.commentable_name

    def test_tag_when_comments_hearing_image(
        self, hearing, image, comment
    ):
        hearing.main_image = image
        comment.image = image
        assert comment.tag == image.commentable_name

    def test_tag_when_comments_alternative_image(
        self, alternative, image, comment
    ):
        alternative.main_image = image
        comment.image = image
        assert comment.tag == image.commentable_name

    def test_tag_when_comments_another_comment(self, comment):
        another_comment = CommentFactory.build()
        comment.comment = another_comment
        assert comment.tag == 'Mielipide'


@pytest.mark.usefixtures('database')
class TestCommentWithDatabase(object):
    @pytest.fixture
    def comment(self):
        return CommentFactory()

    @pytest.mark.parametrize(
        'column_name',
        [
            'created_at',
            'title',
            'lead',
            'body',
            'username',
        ]
    )
    def test_non_nullable_columns(self, column_name, comment):
        assert_non_nullable(comment, column_name)

    def test_created_at_defaults_to_datetime(self):
        assert isinstance(CommentFactory(created_at=None).created_at, datetime)

    def test_updated_at_is_nullable(self, comment):
        assert_nullable(comment, 'updated_at')

    def test_updated_at_defaults_to_datetime(self):
        assert isinstance(CommentFactory(updated_at=None).created_at, datetime)

    def test_title_max_length_is_255(self, comment):
        assert_max_length(comment, 'title', 255)

    def test_title_defaults_to_empty_string(self):
        assert CommentFactory(title=None).title == ''

    def test_lead_defaults_to_empty_string(self):
        assert CommentFactory(lead=None).lead == ''

    def test_body_defaults_to_empty_string(self):
        assert CommentFactory(body=None).body == ''

    def test_username_max_length_is_255(self, comment):
        assert_max_length(comment, 'username', 255)

    def test_username_defaults_to_empty_string(self):
        assert CommentFactory(username=None).username == ''

    def test_uses_versioning(self, comment):
        assert count_versions(comment) == 1


@pytest.mark.usefixtures('database')
class TestCommentCheckConstraint(object):
    def test_comment_must_reference_something(self):
        with pytest.raises(IntegrityError):
            CommentFactory(
                hearing=None,
                alternative=None,
                comment=None,
                image=None
            )

    def test_comment_cant_reference_both_hearing_and_alternative(self):
        with pytest.raises(IntegrityError):
            CommentFactory(
                hearing_id=1,
                alternative_id=1
            )

    def test_comment_cant_reference_both_hearing_and_comment(self):
        with pytest.raises(IntegrityError):
            CommentFactory(
                hearing_id=1,
                comment_id=1
            )

    def test_comment_cant_reference_both_hearing_and_image(self):
        with pytest.raises(IntegrityError):
            CommentFactory(
                hearing_id=1,
                image_id=1
            )

    def test_comment_cant_reference_both_alternative_and_comment(self):
        with pytest.raises(IntegrityError):
            CommentFactory(
                alternative_id=1,
                comment_id=1
            )

    def test_comment_cant_reference_both_alternative_and_image(self):
        with pytest.raises(IntegrityError):
            CommentFactory(
                alternative_id=1,
                image_id=1
            )

    def test_comment_cant_reference_both_comment_and_image(self):
        with pytest.raises(IntegrityError):
            CommentFactory(
                comment_id=1,
                image_id=1
            )
