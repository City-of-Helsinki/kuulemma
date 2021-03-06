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

from datetime import date

from geoalchemy2 import Geometry
from geoalchemy2.shape import from_shape, to_shape
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.orderinglist import ordering_list

from kuulemma.extensions import db

from .alternative import Alternative
from .section import Section
from .question import Question
from .image import Image
from .text_item_mixin import TextItemMixin

TAGS = {
    'hameentie': [
        {'name': 'Liikenne', 'type': 'traffic'},
        {'name': 'Kallio', 'type': 'area'},
        {'name': 'Sörnäinen', 'type': 'area'},
    ],
    'latokartanontie': [
        {'name': 'Liikenne', 'type': 'traffic'},
        {'name': 'Malmi', 'type': 'area'},
    ],
    'maria': [
        {'name': 'Täydennysrakentaminen', 'type': 'building'},
        {'name': 'Kamppi', 'type': 'area'},
        {'name': 'Mechelininkatu', 'type': 'area'},
        {'name': 'Baana', 'type': 'area'},
    ],
    'myllypuronkoulut': [
        {'name': 'Kouluverkko', 'type': 'schools'},
        {'name': 'Myllypuro', 'type': 'area'},
    ],
    'pakilankoulut': [
        {'name': 'Oppilaaksiottoalue', 'type': 'schools'},
        {'name': 'Pakila', 'type': 'area'},
        {'name': 'Torpparinmäki', 'type': 'area'},
    ],
    'pikkuhuopalahti': [
        {'name': 'Kaavoitus', 'type': 'building'},
        {'name': 'Pikku Huopalahti', 'type': 'area'},
    ],
    'sturenkatu': [
        {'name': 'Liikenne', 'type': 'traffic'},
        {'name': 'Alppiharju', 'type': 'area'},
        {'name': 'Vallila', 'type': 'area'},
    ],
    'servicenatsodra': [
        {'name': 'Skolservicenätet', 'type': 'school'},
        {'name': 'Södra området', 'type': 'area'},
    ],
    'kalasatamankoulu': [
        {'name': 'Koulurakentaminen', 'type': 'school'},
        {'name': 'Kalasatama', 'type': 'area'},
    ],
    'vesalankoulut': [
        {'name': 'Kouluverkko', 'type': 'schools'},
        {'name': 'Vesala', 'type': 'area'},
    ],
    'ylamalminkoulut': [
        {'name': 'Kouluverkko', 'type': 'schools'},
        {'name': 'Ylä-Malmi', 'type': 'area'},
    ],
    'kannelmaenkoulut': [
        {'name': 'Kouluverkko', 'type': 'schools'},
        {'name': 'Kannelmäki', 'type': 'area'},
    ],
    'pukinmaenkoulut': [
        {'name': 'Oppilaaksiottoalue', 'type': 'schools'},
        {'name': 'Pukinmäki', 'type': 'area'},
        {'name': 'Malmi', 'type': 'area'},
    ],
    'lauttasaarenkoulut': [
        {'name': 'Koulut', 'type': 'schools'},
        {'name': 'Lauttasaari', 'type': 'area'},
    ],
    'meri-rastila': [
        {'name': 'Kaavoitus', 'type': 'building'},
        {'name': 'Täydennysrakentaminen', 'type': 'building'},
        {'name': 'Meri-Rastila', 'type': 'area'},
        {'name': 'Vuosaari', 'type': 'area'},
    ],
    'hameentiesuunnitelma': [
        {'name': 'Liikenne', 'type': 'traffic'},
        {'name': 'Kallio', 'type': 'area'},
        {'name': 'Sörnäinen', 'type': 'area'},
    ],
    'vuosaarenkoulut': [
        {'name': 'Koulut', 'type': 'schools'},
        {'name': 'Vuosaari', 'type': 'area'},
    ],
    'meilahdenkoulut': [
        {'name': 'Koulut', 'type': 'schools'},
        {'name': 'Meilahti', 'type': 'area'},
    ],
    'kulosaarenostari': [
        {'name': 'Kaavoitus', 'type': 'building'},
        {'name': 'Täydennysrakentaminen', 'type': 'building'},
        {'name': 'Kulosaari', 'type': 'area'},
    ],
    'herttoniemensairaala': [
        {'name': 'Kaavoitus', 'type': 'building'},
        {'name': 'Herttoniemi', 'type': 'area'},
    ],
    'vuosaarenkoulut2': [
        {'name': 'Koulut', 'type': 'schools'},
        {'name': 'Vuosaari', 'type': 'area'},
    ],
    'asuminen': [
        {'name': 'Asuminen', 'type': 'building'},
        {'name': 'Maankäyttö', 'type': 'building'},
        {'name': 'Helsinki', 'type': 'area'},
    ],
    'vuosaarenkoulut3': [
        {'name': 'Koulut', 'type': 'schools'},
        {'name': 'Vuosaari', 'type': 'area'},
    ],
    'digitaalinenhelsinki': [
        {'name': 'Palvelut', 'type': 'services'},
        {'name': 'Helsinki', 'type': 'area'},
    ],
    'gardenianmyynti': [
        {'name': 'Palvelut', 'type': 'services'},
        {'name': 'Viikki', 'type': 'area'},
    ],
    'lauttasaarenuusikoulutila': [
        {'name': 'Koulut', 'type': 'schools'},
        {'name': 'Lauttasaari', 'type': 'area'},
    ],
}


class Hearing(db.Model, TextItemMixin):
    __versioned__ = {}
    __tablename__ = 'hearing'

    id = db.Column(db.Integer, primary_key=True)

    slug = db.Column(
        db.Unicode(255),
        nullable=False,
        unique=True,
        default='',
        server_default=''
    )

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
        Alternative,
        cascade='all, delete-orphan',
        passive_deletes=True,
        backref='hearing',
        order_by='Alternative.position',
        collection_class=ordering_list('position'),
    )

    sections = db.relationship(
        Section,
        cascade='all, delete-orphan',
        passive_deletes=True,
        backref='hearing',
        order_by='Section.position',
        collection_class=ordering_list('position'),
    )

    questions = db.relationship(
        Question,
        cascade='all, delete-orphan',
        passive_deletes=True,
        backref='hearing',
        order_by='Question.position',
        collection_class=ordering_list('position'),
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
        post_update=True,
        backref=db.backref('hearing_main', uselist=False)
    )

    images = db.relationship(
        Image,
        primaryjoin=id == Image.hearing_id,
        cascade='all, delete-orphan',
        passive_deletes=True,
        order_by=Image.position,
        collection_class=ordering_list('position'),
        backref='hearing'
    )

    _area = db.Column(Geometry('POLYGON'))

    @property
    def related_hearing(self):
        return self

    @property
    def commentable_id(self):
        return 'hearing-{id}'.format(id=self.id)

    @property
    def commentable_name(self):
        return 'Koko kuuleminen'

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

    @hybrid_property
    def is_open(self):
        return self.closes_at and self.closes_at >= date.today()

    @property
    def days_open(self):
        if self.closes_at:
            days_open = (self.closes_at - date.today()).days + 1
            return max(0, days_open)
        return 0

    @property
    def tags(self):
        if self.slug in TAGS:
            return TAGS[self.slug]
        return []

    @property
    def all_comments(self):
        from .comment import Comment
        from .image import Image

        alternative_ids = [alternative.id for alternative in self.alternatives]
        alternative_main_image_ids = [
            alternative.main_image_id for alternative in self.alternatives
        ]

        section_ids = [section.id for section in self.sections]
        section_main_image_ids = [
            section.main_image_id for section in self.sections
        ]

        question_ids = [question.id for question in self.questions]
        question_main_image_ids = [
            question.main_image_id for question in self.questions
        ]

        image_criteria = [Image.hearing_id == self.id]
        comment_criteria = [
            Comment.hearing_id == self.id,
            db.and_(
                Comment.image_id == self.main_image_id,
                Comment.image_id.isnot(None)
            )
        ]

        if alternative_main_image_ids:
            image_criteria.append(Image.id.in_(alternative_main_image_ids))

        if section_main_image_ids:
            image_criteria.append(Image.id.in_(section_main_image_ids))

        if question_main_image_ids:
            image_criteria.append(Image.id.in_(question_main_image_ids))

        if alternative_ids:
            image_criteria.append(Image.alternative_id.in_(alternative_ids))
            comment_criteria.append(
                Comment.alternative_id.in_(alternative_ids)
            )

        if section_ids:
            image_criteria.append(Image.section_id.in_(section_ids))
            comment_criteria.append(
                Comment.section_id.in_(section_ids)
            )

        if question_ids:
            image_criteria.append(Image.question_id.in_(question_ids))
            comment_criteria.append(
                Comment.question_id.in_(question_ids)
            )

        hearing_image_ids = db.session.query(Image.id).filter(
            db.or_(*image_criteria)
        )
        comment_criteria.append(Comment.image_id.in_(hearing_image_ids))

        comment_parent_ids = db.session.query(Comment.id).filter(
            db.or_(*comment_criteria)
        )
        comment_criteria.append(Comment.comment_id.in_(comment_parent_ids))
        return Comment.query.filter(db.or_(*comment_criteria))

    @property
    def comment_count(self):
        from .comment import Comment
        return (
            self.all_comments
            .filter(~Comment.is_hidden)
            .count()
        )

    @property
    def comments_for_report(self):
        from .comment import Comment
        return (
            self.all_comments
            .filter(~Comment.is_hidden)
            .order_by(
                Comment.hearing_id,
                Comment.alternative_id,
                Comment.section_id,
                Comment.question_id,
                Comment.image_id,
                Comment.comment_id,
                Comment.id
            )
        )

    @property
    def report_filename(self):
        return '{slug}_raportti_{date}'.format(
            slug=self.slug,
            date=date.today().strftime('%d-%m-%Y')
        )

    @property
    def report_headers(self):
        return [
            'Otsikko',
            'Viittaa',
            'Kirjoittaja',
            'Saapunut',
            'Kannatettu',
            'Mielipide',
        ]

    def get_commentable_sections_string(self):
        """
        Return in string format id, name pairs of all the commentable sections
        related to this hearing.
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

        sections_string = ';'.join(sections)

        for alternative in self.alternatives:
            sections_string += (
                ';' + alternative.get_commentable_sections_string()
            )

        for section in self.sections:
            sections_string += (
                ';' + section.get_commentable_sections_string()
            )

        for question in self.questions:
            sections_string += (
                ';' + question.get_commentable_sections_string()
            )

        return sections_string

    @property
    def area(self):
        if self._area is not None:
            return to_shape(self._area)
        return self._area

    @area.setter
    def area(self, value):
        self._area = from_shape(value)

    @staticmethod
    def _get_polygon_center(polygon):
        from shapely.geometry import Point
        x0, y0, x1, y1 = polygon.bounds
        y = y0 + ((y1 - y0) / 2)
        x = x0 + ((x1 - x0) / 2)
        return Point(x, y)

    @property
    def map_coordinates(self):
        if self.area:
            return self._get_polygon_center(self.area)
        return None

    @property
    def area_as_geoJSON_string(self):
        import json
        from shapely.geometry import mapping
        return json.dumps(mapping(self.area)) or "{}"
