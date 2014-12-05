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

import factory

from kuulemma.models import (
    Alternative,
    Comment,
    Feedback,
    Hearing,
    Image,
    Like,
    User
)
from tests.sqlalchemy_model_factory import SQLAlchemyModelFactory


class AlternativeFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Alternative
    title = factory.Sequence(lambda n: 'Alternative {0}'.format(n))


class HearingFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Hearing
    title = factory.Sequence(lambda n: 'Hearing {0}'.format(n))
    slug = factory.Sequence(lambda n: 'slug-{0}'.format(n))


class CommentFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Comment
    title = factory.Sequence(lambda n: 'Comment {0}'.format(n))
    username = factory.Sequence(lambda n: 'Commenter {0}'.format(n))
    hearing = factory.SubFactory(HearingFactory)


class UserFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = User
    username = 'Luke'
    email = factory.Sequence(lambda n: 'luke%d@skywalker.com' % n)
    # secret-password
    password = (
        '$6$rounds=100000$VdCGUbI5FyS76cdR$WHJrIkhTNx5dEDGMKXngxw5gcj43PbUG5P5'
        'jVsxeEb9oMo.FbknsRnvhpVDTUPxAJeYGg20DKR4LEGpeGO9e2.'
    )


class LikeFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Like
    user = factory.SubFactory(UserFactory)
    comment = factory.SubFactory(CommentFactory)


class ImageFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Image
    filename = 'images/hearings/1/sample-image.jpg'
    caption = 'This is the caption of the sample image.'


class FeedbackFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Feedback
    content = 'This site is superb!'
