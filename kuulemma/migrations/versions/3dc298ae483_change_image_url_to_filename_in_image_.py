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
