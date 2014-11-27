"""Change `image_url` to `filename` in `image` table"""

# revision identifiers, used by Alembic.
revision = '3dc298ae483'
down_revision = '3aa8d3b65ff'

from alembic import op


def upgrade():
    op.alter_column('image', 'image_url', new_column_name='filename')

    conn = op.get_bind()
    rows = conn.execute('SELECT * FROM image')

    for row in rows:
        conn.execute('''
            UPDATE image
            SET filename = '{filename}'
            WHERE id = {id}
        '''.format(
            filename=row['filename'].replace('/static/', ''),
            id=row['id']
        ))


def downgrade():
    conn = op.get_bind()
    rows = conn.execute('SELECT * FROM image')

    for row in rows:
        conn.execute('''
            UPDATE image
            SET filename = '/static/{filename}'
            WHERE id = {id}
        '''.format(
            filename=row['filename'],
            id=row['id']
        ))

    op.alter_column('image', 'filename', new_column_name='image_url')
