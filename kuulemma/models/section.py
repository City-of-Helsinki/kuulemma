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

from sqlalchemy.ext.orderinglist import ordering_list

from kuulemma.extensions import db

from .image import Image
from .text_item_mixin import TextItemMixin


class Section(db.Model, TextItemMixin):
    """
    Implements a hearing subsection, modeled on a hearing alternative.
    """

    __versioned__ = {}
    __tablename__ = 'section'

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
            name='section_main_image_id_fkey'
        )
    )

    main_image = db.relationship(
        Image,
        primaryjoin=main_image_id == Image.id,
        post_update=True,
        backref=db.backref('section_main', uselist=False)
    )

    images = db.relationship(
        Image,
        primaryjoin=id == Image.section_id,
        cascade='all, delete-orphan',
        passive_deletes=True,
        order_by=Image.position,
        collection_class=ordering_list('position'),
        backref='section'
    )

    position = db.Column(db.Integer)

    @property
    def related_hearing(self):
        from .hearing import Hearing
        return Hearing.query.get(self.hearing_id)

    @property
    def letter(self):
        ASCII_INDEX_OF_A = 65
        position = self.position or 0
        return chr(ASCII_INDEX_OF_A + position)

    @property
    def commentable_id(self):
        return 'section-{id}'.format(id=self.id)

    @property
    def commentable_name(self):
        return 'Kysymys {letter}'.format(letter=self.letter)

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

    def get_commentable_sections_string(self):
        """
        Return in string format id, name pairs of all the commentable sections
        related to this alternative.
        """
        sections = []
        sections.append(self.commentable_option)
        if self.images:
            if self.main_image:
                sections.append(
                    self.main_image.commentable_option
                )
            for image in self.images:
                sections.append(
                    image.commentable_option
                )
        return ';'.join(sections)
