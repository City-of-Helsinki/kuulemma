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

"""Add Continuum versioning to `hearing` table"""

# revision identifiers, used by Alembic.
revision = '4b53eb45cfa'
down_revision = '236166b3c41'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'hearing_version',
        sa.Column(
            'id',
            sa.Integer(),
            autoincrement=False,
            nullable=False
        ),
        sa.Column(
            'title',
            sa.Unicode(length=255),
            server_default='',
            autoincrement=False,
            nullable=True
        ),
        sa.Column(
            'lead',
            sa.UnicodeText(),
            server_default='',
            autoincrement=False,
            nullable=True
        ),
        sa.Column(
            'body',
            sa.UnicodeText(),
            server_default='',
            autoincrement=False,
            nullable=True
        ),
        sa.Column(
            'transaction_id',
            sa.BigInteger(),
            autoincrement=False,
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
        op.f('ix_hearing_version_end_transaction_id'),
        'hearing_version',
        ['end_transaction_id'],
        unique=False
    )
    op.create_index(
        op.f('ix_hearing_version_operation_type'),
        'hearing_version',
        ['operation_type'],
        unique=False
    )
    op.create_index(
        op.f('ix_hearing_version_transaction_id'),
        'hearing_version',
        ['transaction_id'],
        unique=False
    )

    op.create_table(
        'transaction',
        sa.Column(
            'issued_at',
            sa.DateTime(),
            nullable=True
        ),
        sa.Column(
            'id',
            sa.BigInteger(),
            nullable=False
        ),
        sa.Column(
            'remote_addr',
            sa.String(length=50),
            nullable=True
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('transaction')
    op.drop_index(
        op.f('ix_hearing_version_transaction_id'),
        table_name='hearing_version'
    )
    op.drop_index(
        op.f('ix_hearing_version_operation_type'),
        table_name='hearing_version'
    )
    op.drop_index(
        op.f('ix_hearing_version_end_transaction_id'),
        table_name='hearing_version'
    )
    op.drop_table('hearing_version')
