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

from flask.ext.login import UserMixin
from sqlalchemy_utils import EmailType, PasswordType

from kuulemma.extensions import db


class User(db.Model, UserMixin):
    __versioned__ = {}
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    is_admin = db.Column(
        db.Boolean(),
        nullable=False,
        default=False,
        server_default='FALSE'
    )

    is_official = db.Column(
        db.Boolean(),
        nullable=False,
        default=False,
        server_default='FALSE'
    )

    email = db.Column(
        EmailType(),
        nullable=False,
        unique=True
    )

    password = db.Column(
        PasswordType(schemes=['pbkdf2_sha512']),
        nullable=False
    )

    date_joined = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    last_seen = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    username = db.Column(
        db.Unicode(255),
        nullable=False,
        default=''
    )

    active = db.Column(
        db.Boolean,
        nullable=False,
        default=False,
        server_default='FALSE'
    )

    def is_active(self):
        return self.active

    def __repr__(self):
        return '<{cls} username={name!r}, email={email!r}>'.format(
            cls=self.__class__.__name__,
            name=self.username,
            email=self.email,
        )

    def __str__(self):
        return self.email

    def get_liked_comment_ids(self, hearing=None):
        if hearing:
            comment_ids = [comment.id for comment in hearing.all_comments]
            return [
                like.comment_id for like in self.likes
                if like.comment_id in comment_ids
            ]

        return [like.comment_id for like in self.likes]
