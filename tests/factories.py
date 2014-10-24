# -*- coding: utf-8 -*-
import factory

from kuulemma.models import Hearing
from tests.sqlalchemy_model_factory import SQLAlchemyModelFactory


class HearingFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Hearing
    title = factory.Sequence(lambda n: u'Hearing {0}'.format(n))
