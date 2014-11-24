"""Add `slug` to `hearing`"""

# revision identifiers, used by Alembic.
revision = '3724320b21a'
down_revision = '1b941d2a7b3'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'hearing',
        sa.Column(
            'slug',
            sa.Unicode(length=255),
            server_default='',
            nullable=False
        )
    )

    op.execute('UPDATE hearing SET slug = hearing.id')
    op.create_unique_constraint(None, 'hearing', ['slug'])

    op.add_column(
        'hearing_version',
        sa.Column(
            'slug',
            sa.Unicode(length=255),
            server_default=''
        )
    )


def downgrade():
    op.drop_column('hearing_version', 'slug')
    op.drop_constraint(None, 'hearing')
    op.drop_column('hearing', 'slug')
