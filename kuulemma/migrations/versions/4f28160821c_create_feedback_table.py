"""Create `feedback` table"""

# revision identifiers, used by Alembic.
revision = '4f28160821c'
down_revision = '3724320b21a'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'feedback',
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
            nullable=True
        ),
        sa.Column(
            'content',
            sa.UnicodeText(),
            server_default='',
            nullable=False
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('feedback')
