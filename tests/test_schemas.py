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

from kuulemma.schemas import CommentSchema
from tests.factories import (
    CommentFactory,
    HearingFactory,
    LikeFactory,
    UserFactory
)


@pytest.mark.usefixtures('database')
def test_comment_serializer():
    hearing = HearingFactory(id=1)
    comment = CommentFactory(
        id=123,
        hearing=hearing,
        title='Awesome title',
        body='So much content.'
    )
    user = UserFactory()
    LikeFactory(user=user, comment=comment)
    schema = CommentSchema()
    schema.contex = {'user': user}
    data, errors = schema.dump(comment)
    assert data == {
        'id': comment.id,
        'title': comment.title,
        'body': comment.body,
        'username': comment.username,
        'created_at': comment.created_at.isoformat() + '+00:00',
        'like_count': comment.like_count,
        'tag': comment.tag,
        'parent_preview': comment.parent_preview,
        'is_hidden': comment.is_hidden,
        'object_type': 'hearing',
        'object_id': hearing.id
    }
