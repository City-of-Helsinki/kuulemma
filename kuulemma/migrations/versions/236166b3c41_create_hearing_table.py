"""Create `hearing` table"""

# revision identifiers, used by Alembic.
revision = '236166b3c41'
down_revision = None

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'hearing',
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
            server_onupdate='now()',
            nullable=True
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
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('hearing')
