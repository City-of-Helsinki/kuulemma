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

"""Add `hearing_id` to `hearing_section`"""

# revision identifiers, used by Alembic.
revision = '47f952cf2c8'
down_revision = '2529792df50'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'hearing_section',
        sa.Column(
            'hearing_id',
            sa.Integer(),
        )
    )
    op.add_column(
        'hearing_section_version',
        sa.Column(
            'hearing_id',
            sa.Integer(),
        )
    )


def downgrade():
    op.drop_column('hearing_section_version', 'hearing_id')
    op.drop_column('hearing_section', 'hearing_id')
