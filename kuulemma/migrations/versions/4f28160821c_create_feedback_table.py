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

"""Create `feedback` table"""

# revision identifiers, used by Alembic.
revision = '4f28160821c'
down_revision = '3724320b21a'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'feedback',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),
        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default='now()',
            nullable=False
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(),
            nullable=True
        ),
        sa.Column(
            'content',
            sa.UnicodeText(),
            server_default='',
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('feedback')
