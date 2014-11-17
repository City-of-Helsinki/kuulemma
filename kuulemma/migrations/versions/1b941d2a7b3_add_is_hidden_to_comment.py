"""Add `is_hidden` to `comment`"""

# revision identifiers, used by Alembic.
revision = '1b941d2a7b3'
down_revision = '2bdb80cdad6'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'comment',
        sa.Column(
            'is_hidden',
            sa.Boolean(),
            server_default='FALSE',
            nullable=False
        )
    )
    op.add_column(
        'comment_version',
        sa.Column(
            'is_hidden',
            sa.Boolean(),
            server_default='FALSE'
        )
    )


def downgrade():
    op.drop_column('comment_version', 'is_hidden')
    op.drop_column('comment', 'is_hidden')
