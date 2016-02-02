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

from flask import Blueprint, render_template

from kuulemma.extensions import db
from kuulemma.models import Hearing

frontpage = Blueprint(
    name='frontpage',
    import_name=__name__,
    url_prefix=''
)


@frontpage.route('/')
def index():
    featured_hearing = (
        Hearing.query
        .filter(Hearing.is_open)
        .order_by(db.asc(Hearing.closes_at))
        .limit(1)
        .first()
    )

    latest_hearings = (
        Hearing.query
        .filter(Hearing.published)
        .order_by(db.desc(Hearing.opens_at))
        .limit(40)
    )

    return render_template(
        'frontpage/index.html',
        featured_hearing=featured_hearing,
        latest_hearings=latest_hearings,
    )
