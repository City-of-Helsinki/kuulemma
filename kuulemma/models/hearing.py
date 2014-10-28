# -*- coding: utf-8 -*-
from datetime import datetime

from inflection import parameterize
from sqlalchemy.sql import func

from kuulemma.extensions import db


class Hearing(db.Model):
    __versioned__ = {}
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

    main_section_id = db.Column(
        db.Integer,
        db.ForeignKey('hearing_section.id')
    )

    main_section = db.relationship(
        'HearingSection',
        uselist=False,
        backref='hearing'
    )

    def __repr__(self):
        return '<{cls} title={title!r}>'.format(
            cls=self.__class__.__name__,
            title=self.title
        )

    @property
    def title(self):
        return self.main_section.title

    @property
    def lead(self):
        return self.main_section.lead

    @property
    def body(self):
        return self.main_section.body

    @property
    def slug(self):
        return parameterize(self.main_section.title)
