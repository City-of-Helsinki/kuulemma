# -*- coding: utf-8 -*-
from kuulemma.models import Hearing
from tests.sqlalchemy_model_factory import SQLAlchemyModelFactory


class HearingFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Hearing
    title = 'Important Hearing'
