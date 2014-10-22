# -*- coding: utf-8 -*-
from ..factories import HearingFactory


class TestHearing(object):
    def test_repr(self):
        hearing = HearingFactory.build()
        expected = '<Hearing title=\'{title}\'>'.format(title=hearing.title)
        assert repr(hearing) == expected
