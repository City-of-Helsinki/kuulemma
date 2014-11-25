# -*- coding: utf-8 -*-
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
        default=False
    )

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
