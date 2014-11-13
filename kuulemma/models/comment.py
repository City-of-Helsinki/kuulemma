# -*- coding: utf-8 -*-
from kuulemma.extensions import db

from .alternative import Alternative
from .hearing import Hearing
from .image import Image
from .text_item_mixin import TextItemMixin


class Comment(db.Model, TextItemMixin):
    __versioned__ = {}
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

    __table_args__ = (db.CheckConstraint(
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
    ), )

    @property
    def like_count(self):
        return len(self.likes)


COMMENTABLE_TYPES = {
    'alternative': Alternative,
    'comment': Comment,
    'image': Image,
    'hearing': Hearing
}
