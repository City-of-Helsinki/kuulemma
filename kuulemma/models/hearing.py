# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.sql import func

from kuulemma.extensions import db


class Hearing(db.Model):
    __tablename__ = 'hearing'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        nullable=True,
        onupdate=datetime.utcnow,
        server_onupdate=func.now()
    )

    title = db.Column(
        db.Unicode(255),
        nullable=False,
        default='',
        server_default=''
    )

    lead = db.Column(
        db.UnicodeText,
        nullable=False,
        default='',
        server_default=''
    )

    body = db.Column(
        db.UnicodeText,
        nullable=False,
        default='',
        server_default=''
    )

    def __repr__(self):
        return '<{cls} title={title!r}>'.format(
            cls=self.__class__.__name__,
            title=self.title
        )
