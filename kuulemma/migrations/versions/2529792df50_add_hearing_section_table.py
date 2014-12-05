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

"""Add `hearing_section` table"""

# revision identifiers, used by Alembic.
revision = '2529792df50'
down_revision = '4b53eb45cfa'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'hearing_section_version',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),
        sa.Column(
            'title',
            sa.Unicode(length=255),
            server_default='',
            nullable=True
        ),
        sa.Column(
            'lead',
            sa.UnicodeText(),
            server_default='',
            nullable=True
        ),
        sa.Column(
            'body',
            sa.UnicodeText(),
            server_default='',
            nullable=True
        ),
        sa.Column(
            'transaction_id',
            sa.BigInteger(),
            nullable=False
        ),
        sa.Column(
            'end_transaction_id',
            sa.BigInteger(),
            nullable=True
        ),
        sa.Column(
            'operation_type',
            sa.SmallInteger(),
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id', 'transaction_id')
    )
    op.create_index(
        op.f('ix_hearing_section_version_end_transaction_id'),
        'hearing_section_version',
        ['end_transaction_id'],
        unique=False
    )
    op.create_index(
        op.f('ix_hearing_section_version_operation_type'),
        'hearing_section_version',
        ['operation_type'],
        unique=False
    )
    op.create_index(
        op.f('ix_hearing_section_version_transaction_id'),
        'hearing_section_version',
        ['transaction_id'],
        unique=False
    )

    op.create_table(
        'hearing_section',
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

    op.add_column(
        'hearing',
        sa.Column(
            'main_section_id',
            sa.Integer(),
            nullable=True
        )
    )
    op.drop_column('hearing', 'title')
    op.drop_column('hearing', 'lead')
    op.drop_column('hearing', 'body')

    op.add_column(
        'hearing_version',
        sa.Column(
            'main_section_id',
            sa.Integer(),
            nullable=True
        )
    )
    op.drop_column('hearing_version', 'title')
    op.drop_column('hearing_version', 'lead')
    op.drop_column('hearing_version', 'body')


def downgrade():
    op.add_column(
        'hearing_version',
        sa.Column(
            'body',
            sa.UnicodeText(),
            server_default='',
            nullable=True
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'lead',
            sa.UnicodeText(),
            server_default='',
            nullable=True
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'title',
            sa.Unicode(length=255),
            server_default='',
            nullable=True
        )
    )
    op.drop_column('hearing_version', 'main_section_id')

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

    op.drop_table('hearing_section')
    op.drop_index(
        op.f('ix_hearing_section_version_transaction_id'),
        table_name='hearing_section_version'
    )
    op.drop_index(
        op.f('ix_hearing_section_version_operation_type'),
        table_name='hearing_section_version'
    )
    op.drop_index(
        op.f('ix_hearing_section_version_end_transaction_id'),
        table_name='hearing_section_version'
    )
    op.drop_table('hearing_section_version')
