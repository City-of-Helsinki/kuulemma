# -*- coding: utf-8 -*-
from datetime import date

from inflection import parameterize

from kuulemma.extensions import db

from .hearing_section import HearingSection
from .text_item_mixin import TextItemMixin


class Hearing(db.Model, TextItemMixin):
    __versioned__ = {}
    __tablename__ = 'hearing'

    opens_at = db.Column(
        db.Date,
        nullable=True,
    )

    closes_at = db.Column(
        db.Date,
        nullable=True,
    )

    published = db.Column(
        db.Boolean(),
        nullable=False,
        default=False,
        server_default='FALSE'
    )

    alternatives = db.relationship(
        HearingSection,
        cascade='all, delete-orphan',
        passive_deletes=True,
        backref='hearing'
    )

    @property
    def slug(self):
        return parameterize(self.title)

    @property
    def days_open(self):
        if self.closes_at:
            days_open = self.closes_at - date.today()
            return max(0, days_open.days)
        return 0
