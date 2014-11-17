"""Add `position` to `alternative`"""

# revision identifiers, used by Alembic.
revision = '2bdb80cdad6'
down_revision = '14051cff79e'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'alternative',
        sa.Column(
            'position',
            sa.Integer()
        )
    )
    op.add_column(
        'alternative_version',
        sa.Column(
            'position',
            sa.Integer()
        )
    )


def downgrade():
    op.drop_column('alternative_version', 'position')
    op.drop_column('alternative', 'position')
