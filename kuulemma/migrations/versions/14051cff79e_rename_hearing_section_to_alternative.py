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

"""Rename `hearing_section` to `alternative`"""

# revision identifiers, used by Alembic.
revision = '14051cff79e'
down_revision = '51051f5b195'

from alembic import op


def upgrade():
    op.rename_table('hearing_section', 'alternative')
    op.rename_table('hearing_section_version', 'alternative_version')

    op.alter_column(
        'comment',
        'hearing_section_id',
        new_column_name='alternative_id'
    )

    op.alter_column(
        'image',
        'hearing_section_id',
        new_column_name='alternative_id'
    )

    op.alter_column(
        'comment_version',
        'hearing_section_id',
        new_column_name='alternative_id'
    )

    op.create_index(op.f(
        'ix_alternative_version_end_transaction_id'),
        'alternative_version',
        ['end_transaction_id'],
        unique=False
    )
    op.create_index(op.f(
        'ix_alternative_version_operation_type'),
        'alternative_version',
        ['operation_type'],
        unique=False
    )
    op.create_index(op.f(
        'ix_alternative_version_transaction_id'),
        'alternative_version',
        ['transaction_id'],
        unique=False
    )
    op.drop_index(
        'ix_hearing_section_version_end_transaction_id',
        table_name='alternative_version'
    )
    op.drop_index(
        'ix_hearing_section_version_operation_type',
        table_name='alternative_version'
    )
    op.drop_index(
        'ix_hearing_section_version_transaction_id',
        table_name='alternative_version'
    )
    op.create_index(
        op.f('ix_image_alternative_id'),
        'image',
        ['alternative_id'],
        unique=False
    )
    op.drop_index(
        'ix_image_hearing_section_id',
        table_name='image'
    )


def downgrade():
    op.drop_index(
        op.f('ix_image_alternative_id'),
        table_name='image'
    )
    op.drop_index(
        op.f('ix_alternative_version_transaction_id'),
        table_name='alternative_version'
    )
    op.drop_index(
        op.f('ix_alternative_version_operation_type'),
        table_name='alternative_version'
    )
    op.drop_index(
        op.f('ix_alternative_version_end_transaction_id'),
        table_name='alternative_version'
    )

    op.rename_table('alternative', 'hearing_section')
    op.rename_table('alternative_version', 'hearing_section_version')

    op.alter_column(
        'comment',
        'alternative_id',
        new_column_name='hearing_section_id'
    )

    op.alter_column(
        'image',
        'alternative_id',
        new_column_name='hearing_section_id'
    )

    op.alter_column(
        'comment_version',
        'alternative_id',
        new_column_name='hearing_section_id'
    )

    op.create_index(
        'ix_image_hearing_section_id',
        'image',
        ['hearing_section_id'],
        unique=False
    )

    op.create_index(
        'ix_hearing_section_version_transaction_id',
        'hearing_section_version',
        ['transaction_id'],
        unique=False
    )
    op.create_index(
        'ix_hearing_section_version_operation_type',
        'hearing_section_version',
        ['operation_type'],
        unique=False
    )
    op.create_index(
        'ix_hearing_section_version_end_transaction_id',
        'hearing_section_version',
        ['end_transaction_id'],
        unique=False
    )
