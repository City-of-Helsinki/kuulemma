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

"""Create `user` table"""

# revision identifiers, used by Alembic.
revision = '375f9baf8d9'
down_revision = '28a01290c0f'

import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils import EmailType, PasswordType


def upgrade():
    op.create_table(
        'user',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),
        sa.Column(
            'is_admin',
            sa.Boolean(),
            server_default='FALSE',
            nullable=False
        ),
        sa.Column(
            'is_official',
            sa.Boolean(),
            server_default='FALSE',
            nullable=False
        ),
        sa.Column(
            'email',
            EmailType(length=255),
            nullable=False
        ),
        sa.Column(
            'password',
            PasswordType,
            nullable=False
        ),
        sa.Column(
            'date_joined',
            sa.DateTime(),
            nullable=False
        ),
        sa.Column(
            'last_seen',
            sa.DateTime(),
            nullable=False
        ),
        sa.Column(
            'username',
            sa.Unicode(length=255),
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    op.create_table(
        'user_version',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),
        sa.Column(
            'is_admin',
            sa.Boolean(),
            server_default='FALSE',
            nullable=True
        ),
        sa.Column(
            'is_official',
            sa.Boolean(),
            server_default='FALSE',
            nullable=True
        ),
        sa.Column(
            'email',
            EmailType(length=255),
            nullable=True
        ),
        sa.Column(
            'password',
            PasswordType,
            nullable=True
        ),
        sa.Column(
            'username',
            sa.Unicode(length=255),
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
        op.f('ix_user_version_end_transaction_id'),
        'user_version',
        ['end_transaction_id'],
        unique=False
    )
    op.create_index(
        op.f('ix_user_version_operation_type'),
        'user_version',
        ['operation_type'],
        unique=False
    )
    op.create_index(
        op.f('ix_user_version_transaction_id'),
        'user_version',
        ['transaction_id'],
        unique=False
    )


def downgrade():
    op.drop_index(
        op.f('ix_user_version_transaction_id'),
        table_name='user_version'
    )
    op.drop_index(
        op.f('ix_user_version_operation_type'),
        table_name='user_version'
    )
    op.drop_index(
        op.f('ix_user_version_end_transaction_id'),
        table_name='user_version'
    )
    op.drop_table('user_version')
    op.drop_table('user')
