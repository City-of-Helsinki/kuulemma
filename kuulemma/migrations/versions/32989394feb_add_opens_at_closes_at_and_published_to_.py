"""Add `opens_at`, `closes_at` and `published` to `hearing`"""

# revision identifiers, used by Alembic.
revision = '32989394feb'
down_revision = '58c672c60a2'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'hearing',
        sa.Column(
            'closes_at',
            sa.Date(),
        )
    )
    op.add_column(
        'hearing',
        sa.Column(
            'opens_at',
            sa.Date(),
        )
    )
    op.add_column(
        'hearing',
        sa.Column(
            'published',
            sa.Boolean(),
            server_default='FALSE',
            nullable=False
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'closes_at',
            sa.Date(),
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'opens_at',
            sa.Date(),
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'published',
            sa.Boolean(),
            server_default='FALSE',
        )
    )


def downgrade():
    op.drop_column('hearing_version', 'published')
    op.drop_column('hearing_version', 'opens_at')
    op.drop_column('hearing_version', 'closes_at')
    op.drop_column('hearing', 'published')
    op.drop_column('hearing', 'opens_at')
    op.drop_column('hearing', 'closes_at')
