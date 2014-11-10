# -*- coding: utf-8 -*-
from sqlalchemy.ext.orderinglist import ordering_list

from kuulemma.extensions import db

from .image import Image
from .text_item_mixin import TextItemMixin


class Alternative(db.Model, TextItemMixin):
    __versioned__ = {}
    __tablename__ = 'alternative'

    id = db.Column(db.Integer, primary_key=True)

    hearing_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'hearing.id',
            ondelete='CASCADE'
        )
    )

    main_image_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'image.id',
            ondelete='CASCADE',
            use_alter=True,
            name='alternative_main_image_id_fkey'
        )
    )

    main_image = db.relationship(
        Image,
        primaryjoin=main_image_id == Image.id,
        post_update=True
    )

    images = db.relationship(
        Image,
        primaryjoin=id == Image.alternative_id,
        cascade='all, delete-orphan',
        passive_deletes=True,
        order_by=Image.position,
        collection_class=ordering_list('position'),
    )

    position = db.Column(db.Integer)

    @property
    def letter(self):
        ASCII_INDEX_OF_A = 65
        position = self.position or 0
        return chr(ASCII_INDEX_OF_A + position)
