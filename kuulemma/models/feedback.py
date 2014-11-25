# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy.sql import func

from kuulemma.extensions import db


class Feedback(db.Model):
    __tablename__ = 'feedback'

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

    content = db.Column(
        db.UnicodeText,
        nullable=False,
        default='',
        server_default=''
    )

    def __repr__(self):
        return '<{cls} content={content!r}>'.format(
            cls=self.__class__.__name__,
            content=self.content,
        )
