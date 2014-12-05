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

"""Add `opens_at`, `closes_at` and `published` to `hearing`"""

# revision identifiers, used by Alembic.
revision = '32989394feb'
down_revision = '58c672c60a2'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'hearing',
        sa.Column(
            'closes_at',
            sa.Date(),
        )
    )
    op.add_column(
        'hearing',
        sa.Column(
            'opens_at',
            sa.Date(),
        )
    )
    op.add_column(
        'hearing',
        sa.Column(
            'published',
            sa.Boolean(),
            server_default='FALSE',
            nullable=False
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'closes_at',
            sa.Date(),
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'opens_at',
            sa.Date(),
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'published',
            sa.Boolean(),
            server_default='FALSE',
        )
    )


def downgrade():
    op.drop_column('hearing_version', 'published')
    op.drop_column('hearing_version', 'opens_at')
    op.drop_column('hearing_version', 'closes_at')
    op.drop_column('hearing', 'published')
    op.drop_column('hearing', 'opens_at')
    op.drop_column('hearing', 'closes_at')
