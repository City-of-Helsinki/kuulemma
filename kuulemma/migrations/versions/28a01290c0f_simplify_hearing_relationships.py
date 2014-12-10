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

"""Simplify `hearing` relationships"""

# revision identifiers, used by Alembic.
revision = '28a01290c0f'
down_revision = '4df00082a4d'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'hearing',
        sa.Column(
            'body',
            sa.UnicodeText(),
            server_default='',
            nullable=False
        )
    )
    op.add_column(
        'hearing',
        sa.Column(
            'lead',
            sa.UnicodeText(),
            server_default='',
            nullable=False
        )
    )
    op.add_column(
        'hearing',
        sa.Column(
            'title',
            sa.Unicode(length=255),
            server_default='',
            nullable=False
        )
    )
    op.drop_column('hearing', 'main_section_id')

    op.add_column(
        'hearing_version',
        sa.Column(
            'body',
            sa.UnicodeText(),
            server_default='',
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'lead',
            sa.UnicodeText(),
            server_default='',
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'title',
            sa.Unicode(length=255),
            server_default='',
        )
    )
    op.drop_column('hearing_version', 'main_section_id')

    op.create_foreign_key(
        'hearing_section_hearing_id_fkey',
        'hearing_section',
        'hearing',
        ['hearing_id'],
        ['id'],
        ondelete='CASCADE'
    )


def downgrade():
    op.add_column(
        'hearing_version',
        sa.Column(
            'main_section_id',
            sa.INTEGER(),
        )
    )
    op.drop_column('hearing_version', 'title')
    op.drop_column('hearing_version', 'lead')
    op.drop_column('hearing_version', 'body')

    op.add_column(
        'hearing',
        sa.Column(
            'main_section_id',
            sa.INTEGER(),
        )
    )
    op.drop_column('hearing', 'title')
    op.drop_column('hearing', 'lead')
    op.drop_column('hearing', 'body')

    op.drop_constraint('hearing_section_hearing_id_fkey', 'hearing_section')
