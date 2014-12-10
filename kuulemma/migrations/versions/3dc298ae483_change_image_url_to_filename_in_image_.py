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

"""Change `image_url` to `filename` in `image` table"""

# revision identifiers, used by Alembic.
revision = '3dc298ae483'
down_revision = '3aa8d3b65ff'

from alembic import op


def upgrade():
    op.alter_column('image', 'image_url', new_column_name='filename')

    op.execute(
        '''
        UPDATE image SET filename = regexp_replace(filename, '^/static/', '')
        '''
    )


def downgrade():
    op.execute(
        '''
        UPDATE image SET filename = CONCAT('/static/', filename)
        '''
    )

    op.alter_column('image', 'filename', new_column_name='image_url')
