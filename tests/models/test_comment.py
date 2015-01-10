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

from datetime import datetime

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy_continuum.utils import count_versions
from sqlalchemy_utils import (
    assert_max_length,
    assert_non_nullable,
    assert_nullable
)

from kuulemma.extensions import db

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

    def test_commentable_name(self, comment):
        expected = 'Mielipide - {title}'.format(title=comment.title)
        assert comment.commentable_name == expected

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

    def test_parent_preview_when_comments_another_comment(self, comment):
        another_comment = CommentFactory.build(body='Lorem ipsum...')
        comment.comment = another_comment
        assert comment.parent_preview == another_comment.body

    def test_parent_preview_when_comments_something_else_than_comments(
        self, hearing, comment
    ):
        comment.hearing = hearing
        assert comment.parent_preview == ''


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
            'is_hidden',
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

    def test_is_hidden_defaults_to_false(self):
        assert CommentFactory(is_hidden=None).is_hidden is False

    def test_uses_versioning(self, comment):
        assert count_versions(comment) == 1

    def test_like_count(self, comment):
        expected = 2
        for _ in range(expected):
            comment.likes.append(LikeFactory())
        db.session.commit()
        assert comment.like_count == expected


@pytest.mark.usefixtures('database')
class TestRelatedHearingProperty(object):
    @pytest.fixture
    def hearing(self):
        return HearingFactory.build()

    @pytest.fixture
    def alternative(self, hearing):
        return AlternativeFactory(hearing=hearing)

    @pytest.fixture
    def image(self):
        return ImageFactory.build()

    @pytest.fixture
    def another_comment(self, hearing):
        return CommentFactory(hearing=hearing)

    def test_should_return_hearing_if_comments_on_hearing(self, hearing):
        comment = CommentFactory(hearing=hearing)
        assert comment.related_hearing == hearing

    def test_should_return_hearing_if_comments_on_alternative(
        self, hearing, alternative, image
    ):
        comment = CommentFactory(hearing=None, alternative=alternative)
        assert comment.related_hearing == hearing

    def test_should_return_hearing_if_comments_on_image(
        self, hearing, image
    ):
        hearing.main_image = image
        comment = CommentFactory(hearing=None, image=image)
        assert comment.related_hearing == hearing

    def test_should_return_hearing_if_comments_on_another_comment(
        self, hearing, another_comment
    ):
        comment = CommentFactory(hearing=None, comment=another_comment)
        assert comment.related_hearing == hearing


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


@pytest.mark.usefixtures('database')
class TestCsvValueArrayProperty(object):
    @pytest.fixture
    def comment(self):
        return CommentFactory(body='This is a mock comment!')

    def test_should_have_title_as_first_value(self, comment):
        assert comment.csv_value_array[0] == comment.title

    def test_should_have_comments_on_name_as_second_value(self, comment):
        assert (
            comment.csv_value_array[1] == comment.comments_on.commentable_name
        )

    def test_should_have_username_as_third_value(self, comment):
        assert comment.csv_value_array[2] == comment.username

    def test_should_have_created_at_in_right_format_as_fourth_value(
        self, comment
    ):
        expected = comment.created_at.strftime('%d.%m.%Y klo %H:%M')
        assert comment.csv_value_array[3] == expected

    def test_should_have_like_count_as_fifth_value(self, comment):
        assert comment.csv_value_array[4] == comment.like_count

    def test_should_have_body_as_sixt_value(self, comment):
        assert comment.csv_value_array[5] == comment.body
