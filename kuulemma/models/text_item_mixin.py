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


class TextItemMixin(object):
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
