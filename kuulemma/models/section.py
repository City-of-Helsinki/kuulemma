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
from .alternative import Alternative


class Section(Alternative):
    """
    Implements a hearing subsection, modeled on a hearing alternative.
    """

    __tablename__ = 'section'

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

    @property
    def commentable_id(self):
        return 'section-{id}'.format(id=self.id)

    @property
    def commentable_name(self):
        return 'Osa-alue {letter}'.format(letter=self.letter)
