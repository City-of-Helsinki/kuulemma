# -*- coding: utf-8 -*-
# Kuulemma
# Copyright (C) 2014, Fast Monkeys Oy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

    filename = db.Column(
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
        return '<{cls} filename={filename!r}>'.format(
            cls=self.__class__.__name__,
            filename=self.filename,
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
    def related_hearing(self):
        return self.belongs_to.related_hearing

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
