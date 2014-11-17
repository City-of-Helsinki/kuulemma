# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.sql import func

from kuulemma.extensions import db


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=True,
        onupdate=datetime.utcnow,
        server_onupdate=func.now()
    )

    hearing_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'hearing.id',
            ondelete='CASCADE'
        ),
        index=True
    )

    alternative_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'alternative.id',
            ondelete='CASCADE'
        ),
        index=True
    )

    image_url = db.Column(
        db.Unicode(255),
        nullable=False,
        default='',
        server_default=''
    )

    caption = db.Column(
        db.UnicodeText,
        nullable=False,
        default='',
        server_default=''
    )

    position = db.Column(db.Integer)

    __table_args__ = (db.CheckConstraint(
        db.or_(
            db.and_(
                hearing_id.is_(None),
                alternative_id.is_(None),
                position.is_(None),
            ),
            db.and_(
                hearing_id.isnot(None),
                alternative_id.is_(None),
                position >= 0
            ),
            db.and_(
                hearing_id.is_(None),
                alternative_id.isnot(None),
                position >= 0
            ),
        )
    ), )

    def __repr__(self):
        return '<{cls} image_url={image_url!r}>'.format(
            cls=self.__class__.__name__,
            image_url=self.image_url,
        )

    @property
    def belongs_to(self):
        if self.hearing:
            return self.hearing
        if self.hearing_main:
            return self.hearing_main
        if self.alternative:
            return self.alternative
        if self.alternative_main:
            return self.alternative_main

    @property
    def is_main_image(self):
        return not (self.hearing_id or self.alternative_id)

    @property
    def number(self):
        if self.is_main_image:
            return 1
        return self.position + 2

    @property
    def commentable_id(self):
        return 'image-{id}'.format(id=self.id)

    @property
    def commentable_name(self):
        return '{context} Kuva {number}'.format(
            context=self.belongs_to.commentable_name,
            number=self.number
        )

    @property
    def commentable_option(self):
        """
        Returns a "id:name" string representation that can be used in the
        frontend when commenting on this section.
        """
        return '{id}:{name}'.format(
            id=self.commentable_id,
            name=self.commentable_name
        )
