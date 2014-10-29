"""Add `hearing_id` to `hearing_section`"""

# revision identifiers, used by Alembic.
revision = '47f952cf2c8'
down_revision = '2529792df50'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.add_column(
        'hearing_section',
        sa.Column(
            'hearing_id',
            sa.Integer(),
        )
    )
    op.add_column(
        'hearing_section_version',
        sa.Column(
            'hearing_id',
            sa.Integer(),
        )
    )


def downgrade():
    op.drop_column('hearing_section_version', 'hearing_id')
    op.drop_column('hearing_section', 'hearing_id')
