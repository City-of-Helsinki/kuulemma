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

"""Add map_coordenates and area to hearings"""

# revision identifiers, used by Alembic.
revision = '3aa8d3b65ff'
down_revision = '15b72abdb27'

import geoalchemy2 as ga
import sqlalchemy as sa
from alembic import op


def upgrade():
    op.execute('CREATE EXTENSION postgis')
    op.add_column(
        'hearing',
        sa.Column(
            '_area',
            ga.Geometry(geometry_type='POLYGON'),
            nullable=True
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            '_area',
            ga.Geometry(geometry_type='POLYGON'),
            autoincrement=False,
            nullable=True
        )
    )


def downgrade():
    op.drop_column('hearing_version', '_area')
    op.drop_column('hearing', '_area')
    op.execute('DROP EXTENSION postgis')
