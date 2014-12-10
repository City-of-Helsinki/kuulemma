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
