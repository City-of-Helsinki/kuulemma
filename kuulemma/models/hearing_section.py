# -*- coding: utf-8 -*-
from sqlalchemy.ext.orderinglist import ordering_list

from kuulemma.extensions import db

from .image import Image
from .text_item_mixin import TextItemMixin


class HearingSection(db.Model, TextItemMixin):
    __versioned__ = {}
    __tablename__ = 'hearing_section'

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
            name='hearing_section_main_image_id_fkey'
        )
    )

    main_image = db.relationship(
        Image,
        primaryjoin=main_image_id == Image.id,
        post_update=True
    )

    images = db.relationship(
        Image,
        primaryjoin=id == Image.hearing_section_id,
        cascade='all, delete-orphan',
        passive_deletes=True,
        order_by='Image.position',
        collection_class=ordering_list('position'),
    )
