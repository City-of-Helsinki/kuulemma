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

"""Add `slug` to `hearing`"""

# revision identifiers, used by Alembic.
revision = '3724320b21a'
down_revision = '1b941d2a7b3'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'hearing',
        sa.Column(
            'slug',
            sa.Unicode(length=255),
            server_default='',
            nullable=False
        )
    )

    op.execute('UPDATE hearing SET slug = hearing.id')
    op.create_unique_constraint(None, 'hearing', ['slug'])

    op.add_column(
        'hearing_version',
        sa.Column(
            'slug',
            sa.Unicode(length=255),
            server_default=''
        )
    )


def downgrade():
    op.drop_column('hearing_version', 'slug')
    op.drop_constraint(None, 'hearing')
    op.drop_column('hearing', 'slug')
