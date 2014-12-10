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

"""Add `like_count` column to `comment` table."""

revision = '10f5abcd410'
down_revision = '3dc298ae483'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'comment',
        sa.Column(
            'like_count',
            sa.Integer(),
            server_default='0',
            nullable=True
        )
    )
    op.execute(
        '''UPDATE comment SET like_count = (
            SELECT COUNT(1) FROM "like" WHERE "like".comment_id = comment.id
        )
        '''
    )
    op.alter_column('comment', 'like_count', nullable=False)
    op.create_index('ix_comment_like_count', 'comment', ['like_count', 'id'])


def downgrade():
    op.drop_index('ix_comment_like_count')
    op.drop_column('comment', 'like_count')
