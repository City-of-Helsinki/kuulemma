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

"""Add `is_hidden` to `comment`"""

# revision identifiers, used by Alembic.
revision = '1b941d2a7b3'
down_revision = '2bdb80cdad6'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'comment',
        sa.Column(
            'is_hidden',
            sa.Boolean(),
            server_default='FALSE',
            nullable=False
        )
    )
    op.add_column(
        'comment_version',
        sa.Column(
            'is_hidden',
            sa.Boolean(),
            server_default='FALSE'
        )
    )


def downgrade():
    op.drop_column('comment_version', 'is_hidden')
    op.drop_column('comment', 'is_hidden')
