# -*- coding: utf-8 -*-
from factory import Factory

from kuulemma.models import Hearing


class HearingFactory(Factory):
    FACTORY_FOR = Hearing
    title = 'Important Hearing'
