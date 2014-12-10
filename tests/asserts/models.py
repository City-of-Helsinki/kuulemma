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

import pytest
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError

from kuulemma.extensions import db


def assert_unique(factory, field):
    obj = factory()
    obj2 = factory()
    table = inspect(obj2.__class__).columns[field].table
    query = table.update().values(**{field: getattr(obj, field)})
    with pytest.raises(IntegrityError):
        db.session.execute(query)
