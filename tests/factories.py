# -*- coding: utf-8 -*-
import factory

from kuulemma.models import Comment, Hearing, HearingSection, Like, User
from tests.sqlalchemy_model_factory import SQLAlchemyModelFactory


class HearingSectionFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = HearingSection
    title = factory.Sequence(lambda n: u'Alternative {0}'.format(n))


class HearingFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Hearing
    title = factory.Sequence(lambda n: u'Hearing {0}'.format(n))


class CommentFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Comment
    title = factory.Sequence(lambda n: u'Comment {0}'.format(n))
    username = factory.Sequence(lambda n: u'Commenter {0}'.format(n))
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
