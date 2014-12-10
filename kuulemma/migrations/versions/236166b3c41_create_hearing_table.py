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

"""Create `hearing` table"""

# revision identifiers, used by Alembic.
revision = '236166b3c41'
down_revision = None

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'hearing',
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
            server_onupdate='now()',
            nullable=True
        ),
        sa.Column(
            'title',
            sa.Unicode(length=255),
            server_default='',
            nullable=False
        ),
        sa.Column(
            'lead',
            sa.UnicodeText(),
            server_default='',
            nullable=False
        ),
        sa.Column(
            'body',
            sa.UnicodeText(),
            server_default='',
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('hearing')
