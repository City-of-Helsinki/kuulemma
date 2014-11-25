"""add active column to user table"""

# revision identifiers, used by Alembic.
revision = '15b72abdb27'
down_revision = '4f28160821c'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'user',
        sa.Column(
            'active',
            sa.Boolean,
            nullable=False,
            server_default='FALSE'
        )
    )
    op.add_column(
        'user_version',
        sa.Column(
            'active',
            sa.Boolean,
            autoincrement=False,
            nullable=True
        )
    )

    op.execute('UPDATE "user" set active = True')


def downgrade():
    op.drop_column('user_version', 'active')
    op.drop_column('user', 'active')
