# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.sql import func

from kuulemma.extensions import db

from .comment import Comment
from .user import User


class Like(db.Model):
    __tablename__ = 'like'

    __table_args__ = (
        db.UniqueConstraint('user_id', 'comment_id'),
    )

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now()
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            User.id,
            ondelete='CASCADE'
        ),
        nullable=False
    )

    user = db.relationship(
        User,
        backref=db.backref(
            'likes',
            cascade='all, delete-orphan',
            passive_deletes=True
        )
    )

    comment_id = db.Column(
        db.Integer,
        db.ForeignKey(
            Comment.id,
            ondelete='CASCADE'
        ),
        nullable=False
    )

    comment = db.relationship(
        Comment,
        backref=db.backref(
            'likes',
            cascade='all, delete-orphan',
            passive_deletes=True
        )
    )

    def __repr__(self):
        return '<{cls} user_id={user_id!r}, comment_id={comment_id!r}>'.format(
            cls=self.__class__.__name__,
            user_id=self.user_id,
            comment_id=self.comment_id
        )
