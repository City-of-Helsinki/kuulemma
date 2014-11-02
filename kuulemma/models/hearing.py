# -*- coding: utf-8 -*-
from inflection import parameterize

from kuulemma.extensions import db

from .hearing_section import HearingSection
from .text_item_mixin import TextItemMixin


class Hearing(db.Model, TextItemMixin):
    __versioned__ = {}
    __tablename__ = 'hearing'

    alternatives = db.relationship(
        HearingSection,
        cascade='all, delete-orphan',
        passive_deletes=True,
        backref='hearing'
    )

    @property
    def slug(self):
        return parameterize(self.title)
