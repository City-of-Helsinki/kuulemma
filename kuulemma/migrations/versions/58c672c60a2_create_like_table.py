"""Create `like` table"""

# revision identifiers, used by Alembic.
revision = '58c672c60a2'
down_revision = '375f9baf8d9'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'like',
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
            'comment_id',
            sa.Integer(),
            nullable=False
        ),
        sa.Column(
            'user_id',
            sa.Integer(),
            nullable=False
        ),
        sa.ForeignKeyConstraint(
            ['comment_id'],
            ['comment.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user.id'],
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'comment_id')
    )


def downgrade():
    op.drop_table('like')
