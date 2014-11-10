# -*- coding: utf-8 -*-
from datetime import date

from inflection import parameterize
from sqlalchemy.ext.orderinglist import ordering_list

from kuulemma.extensions import db

from .hearing_section import HearingSection
from .image import Image
from .text_item_mixin import TextItemMixin


class Hearing(db.Model, TextItemMixin):
    __versioned__ = {}
    __tablename__ = 'hearing'

    id = db.Column(db.Integer, primary_key=True)

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

    main_image_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'image.id',
            ondelete='CASCADE',
            use_alter=True,
            name='hearing_main_image_id_fkey'
        )
    )

    main_image = db.relationship(
        Image,
        primaryjoin=main_image_id == Image.id,
        post_update=True
    )

    images = db.relationship(
        Image,
        primaryjoin=id == Image.hearing_id,
        cascade='all, delete-orphan',
        passive_deletes=True,
        order_by=Image.position,
        collection_class=ordering_list('position'),
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
