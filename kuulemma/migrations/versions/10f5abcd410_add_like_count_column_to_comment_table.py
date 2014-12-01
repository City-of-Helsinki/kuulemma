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
