# -*- coding: utf-8 -*-
from kuulemma.extensions import db

from .hearing import Hearing
from .hearing_section import HearingSection
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

    hearing_section_id = db.Column(
        db.Integer,
        db.ForeignKey(
            HearingSection.id,
            ondelete='CASCADE'
        ),
    )

    hearing_section = db.relationship(
        HearingSection,
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
                hearing_section_id.is_(None)
            ),
            db.and_(
                comment_id.is_(None),
                hearing_id.isnot(None),
                hearing_section_id.is_(None)
            ),
            db.and_(
                comment_id.is_(None),
                hearing_id.is_(None),
                hearing_section_id.isnot(None)
            )
        )
    ), )

    @property
    def like_count(self):
        return len(self.likes)
