# -*- coding: utf-8 -*-
from kuulemma.extensions import db

from .text_item_mixin import TextItemMixin


class HearingSection(db.Model, TextItemMixin):
    __versioned__ = {}
    __tablename__ = 'hearing_section'

    hearing_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'hearing.id',
            ondelete='CASCADE'
        )
    )
