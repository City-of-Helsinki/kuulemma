# -*- coding: utf-8 -*-
from datetime import date

from inflection import parameterize
from sqlalchemy.ext.orderinglist import ordering_list

from kuulemma.extensions import db

from .alternative import Alternative
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
        Alternative,
        cascade='all, delete-orphan',
        passive_deletes=True,
        backref='hearing',
        order_by='Alternative.position',
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

    @property
    def slug(self):
        return parameterize(self.title)

    @property
    def days_open(self):
        if self.closes_at:
            days_open = self.closes_at - date.today()
            return max(0, days_open.days)
        return 0

    @property
    def all_comments(self):
        from .comment import Comment
        from .image import Image

        alternative_ids = [alternative.id for alternative in self.alternatives]
        alternative_main_image_ids = [
            alternative.main_image_id for alternative in self.alternatives
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

        if alternative_ids:
            image_criteria.append(Image.alternative_id.in_(alternative_ids))
            comment_criteria.append(
                Comment.alternative_id.in_(alternative_ids)
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

    def get_commentable_sections_string(self):
        """
        Return in string format id, name pairs of all the commentable sections
        related to this hearing.
        """
        sections = []
        sections.append(self.commentable_option)
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

        return sections_string
