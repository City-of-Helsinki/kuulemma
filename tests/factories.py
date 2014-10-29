# -*- coding: utf-8 -*-
import factory

from kuulemma.models import Comment, Hearing, HearingSection
from tests.sqlalchemy_model_factory import SQLAlchemyModelFactory


class HearingSectionFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = HearingSection
    title = factory.Sequence(lambda n: u'Hearing {0}'.format(n))


class HearingFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Hearing
    main_section = factory.SubFactory(HearingSectionFactory)


class CommentFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Comment
    title = factory.Sequence(lambda n: u'Comment {0}'.format(n))
    username = factory.Sequence(lambda n: u'Commenter {0}'.format(n))
    hearing = factory.SubFactory(HearingFactory)
