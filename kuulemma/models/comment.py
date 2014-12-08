# -*- coding: utf-8 -*-
from sqlalchemy_utils import aggregated

from kuulemma.extensions import db

from .alternative import Alternative
from .hearing import Hearing
from .image import Image
from .text_item_mixin import TextItemMixin


class Comment(db.Model, TextItemMixin):
    __versioned__ = {
        'exclude': ['like_count']
    }
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)

    hearing_id = db.Column(
        db.Integer,
        db.ForeignKey(
            Hearing.id,
            ondelete='CASCADE'
        ),
    )

    hearing = db.relationship(
        Hearing,
        backref=db.backref(
            'comments',
            cascade='all, delete-orphan',
            passive_deletes=True
        )
    )

    comment_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'comment.id',
            ondelete='CASCADE'
        ),
    )

    comment = db.relationship(
        'Comment',
        remote_side=[id],
        backref=db.backref(
            'comments',
            cascade='all, delete-orphan',
            passive_deletes=True
        )
    )

    alternative_id = db.Column(
        db.Integer,
        db.ForeignKey(
            Alternative.id,
            ondelete='CASCADE'
        ),
    )

    alternative = db.relationship(
        Alternative,
        backref=db.backref(
            'comments',
            cascade='all, delete-orphan',
            passive_deletes=True
        )
    )

    image_id = db.Column(
        db.Integer,
        db.ForeignKey(
            Image.id,
            ondelete='CASCADE'
        ),
        index=True
    )

    image = db.relationship(
        Image,
        backref=db.backref(
            'comments',
            cascade='all, delete-orphan',
            passive_deletes=True
        )
    )

    username = db.Column(
        db.Unicode(255),
        nullable=False,
        default='',
        server_default=''
    )

    is_hidden = db.Column(
        db.Boolean(),
        nullable=False,
        default=False,
        server_default='FALSE'
    )

    @aggregated(
        'likes',
        db.Column(
            db.Integer,
            default=0,
            server_default='0',
            nullable=False
        )
    )
    def like_count(self):
        return db.func.count('1')

    __table_args__ = (
        db.CheckConstraint(
            db.or_(
                db.and_(
                    comment_id.isnot(None),
                    hearing_id.is_(None),
                    alternative_id.is_(None),
                    image_id.is_(None)
                ),
                db.and_(
                    comment_id.is_(None),
                    hearing_id.isnot(None),
                    alternative_id.is_(None),
                    image_id.is_(None)
                ),
                db.and_(
                    comment_id.is_(None),
                    hearing_id.is_(None),
                    alternative_id.isnot(None),
                    image_id.is_(None)
                ),
                db.and_(
                    comment_id.is_(None),
                    hearing_id.is_(None),
                    alternative_id.is_(None),
                    image_id.isnot(None)
                )
            )
        ),
        db.Index(
            'ix_comment_like_count',
            'like_count',
            'id'
        )
    )

    @property
    def comments_on(self):
        if self.hearing:
            return self.hearing
        if self.alternative:
            return self.alternative
        if self.image:
            return self.image
        if self.comment:
            return self.comment
        return None

    @property
    def commentable_name(self):
        return 'Mielipide - {title}'.format(title=self.title)

    @property
    def object_type(self):
        return self.comments_on.__class__.__tablename__

    @property
    def object_id(self):
        return self.comments_on.id

    @property
    def tag(self):
        if self.alternative:
            return self.alternative.commentable_name
        if self.image:
            return self.image.commentable_name
        if self.comment:
            return 'Mielipide'
        return ''

    @property
    def parent_preview(self):
        if self.comment:
            return self.comment.body
        return ''

    @property
    def csv_value_array(self):
        return [
            self.title,
            self.comments_on.commentable_name,
            self.username,
            self.created_at.strftime('%d.%m.%Y klo %H:%M'),
            self.like_count,
            self.body,
        ]


COMMENTABLE_TYPES = {
    'alternative': Alternative,
    'comment': Comment,
    'image': Image,
    'hearing': Hearing
}
