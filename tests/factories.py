# -*- coding: utf-8 -*-
import factory

from kuulemma.models import Hearing, HearingSection
from tests.sqlalchemy_model_factory import SQLAlchemyModelFactory


class HearingSectionFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = HearingSection
    title = factory.Sequence(lambda n: u'Hearing {0}'.format(n))


class HearingFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Hearing
    main_section = factory.SubFactory(HearingSectionFactory)
