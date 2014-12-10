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
from sqlalchemy.exc import IntegrityError
from sqlalchemy_utils import assert_non_nullable

from kuulemma.models import Like

from ..factories import CommentFactory, LikeFactory, UserFactory


@pytest.mark.usefixtures('database')
class TestLikeWithDatabase(object):
    @pytest.fixture
    def like(self):
        return LikeFactory()

    def test_repr(self, like):
        expected = (
            '<Like user_id={user_id}, comment_id={comment_id}>'
            .format(
                user_id=like.user_id,
                comment_id=like.comment_id
            )
        )
        assert repr(like) == expected

    @pytest.mark.parametrize(
        'column_name',
        [
            'created_at',
            'user_id',
            'comment_id',
        ]
    )
    def test_non_nullable_columns(self, column_name, like):
        assert_non_nullable(like, column_name)

    def test_user_comment_combination_should_be_unique(self):
        user = UserFactory.build()
        comment = CommentFactory.build()
        LikeFactory(user=user, comment=comment)
        with pytest.raises(IntegrityError):
            LikeFactory(user=user, comment=comment)
            assert Like.query.count() == 1
