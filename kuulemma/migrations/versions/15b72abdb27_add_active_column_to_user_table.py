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

"""add active column to user table"""

# revision identifiers, used by Alembic.
revision = '15b72abdb27'
down_revision = '4f28160821c'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'user',
        sa.Column(
            'active',
            sa.Boolean,
            nullable=False,
            server_default='FALSE'
        )
    )
    op.add_column(
        'user_version',
        sa.Column(
            'active',
            sa.Boolean,
            autoincrement=False,
            nullable=True
        )
    )

    op.execute('UPDATE "user" set active = True')


def downgrade():
    op.drop_column('user_version', 'active')
    op.drop_column('user', 'active')
