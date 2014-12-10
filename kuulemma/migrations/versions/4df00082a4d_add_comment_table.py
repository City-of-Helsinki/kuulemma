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

"""Add `comment` table"""

# revision identifiers, used by Alembic.
revision = '4df00082a4d'
down_revision = '47f952cf2c8'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'comment_version',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),
        sa.Column(
            'title',
            sa.Unicode(length=255),
            server_default='',
        ),
        sa.Column(
            'lead',
            sa.UnicodeText(),
            server_default='',
        ),
        sa.Column(
            'body',
            sa.UnicodeText(),
            server_default='',
        ),
        sa.Column(
            'hearing_id',
            sa.Integer(),
        ),
        sa.Column(
            'comment_id',
            sa.Integer(),
        ),
        sa.Column(
            'hearing_section_id',
            sa.Integer(),
        ),
        sa.Column(
            'username',
            sa.Unicode(length=255),
            server_default='',
        ),
        sa.Column(
            'transaction_id',
            sa.BigInteger(),
            nullable=False
        ),
        sa.Column(
            'end_transaction_id',
            sa.BigInteger(),
        ),
        sa.Column(
            'operation_type',
            sa.SmallInteger(),
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id', 'transaction_id')
    )

    op.create_index(
        op.f('ix_comment_version_end_transaction_id'),
        'comment_version',
        ['end_transaction_id'],
        unique=False
    )
    op.create_index(
        op.f('ix_comment_version_operation_type'),
        'comment_version',
        ['operation_type'],
        unique=False
    )
    op.create_index(
        op.f('ix_comment_version_transaction_id'),
        'comment_version',
        ['transaction_id'],
        unique=False
    )

    op.create_table(
        'comment',
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
        sa.Column(
            'hearing_id',
            sa.Integer(),
        ),
        sa.Column(
            'comment_id',
            sa.Integer(),
        ),
        sa.Column(
            'hearing_section_id',
            sa.Integer(),
        ),
        sa.Column(
            'username',
            sa.Unicode(length=255),
            server_default='',
            nullable=False
        ),
        sa.CheckConstraint(
            '(comment.comment_id IS NOT NULL '
            'AND comment.hearing_id IS NULL '
            'AND comment.hearing_section_id IS NULL) '
            'OR '
            '(comment.comment_id IS NULL '
            'AND comment.hearing_id IS NOT NULL '
            'AND comment.hearing_section_id IS NULL) '
            'OR '
            '(comment.comment_id IS NULL '
            'AND comment.hearing_id IS NULL '
            'AND comment.hearing_section_id IS NOT NULL)'
        ),
        sa.ForeignKeyConstraint(
            ['comment_id'],
            ['comment.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['hearing_id'],
            ['hearing.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['hearing_section_id'],
            ['hearing_section.id'],
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('comment')
    op.drop_index(
        op.f('ix_comment_version_transaction_id'),
        table_name='comment_version'
    )
    op.drop_index(
        op.f('ix_comment_version_operation_type'),
        table_name='comment_version'
    )
    op.drop_index(
        op.f('ix_comment_version_end_transaction_id'),
        table_name='comment_version'
    )
    op.drop_table('comment_version')
