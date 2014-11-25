"""Add map_coordenates and area to hearings"""

# revision identifiers, used by Alembic.
revision = '3aa8d3b65ff'
down_revision = '15b72abdb27'

import geoalchemy2 as ga
import sqlalchemy as sa
from alembic import op


def upgrade():
    op.execute('CREATE EXTENSION postgis')
    op.add_column(
        'hearing',
        sa.Column(
            '_area',
            ga.Geometry(geometry_type='POLYGON'),
            nullable=True
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            '_area',
            ga.Geometry(geometry_type='POLYGON'),
            autoincrement=False,
            nullable=True
        )
    )


def downgrade():
    op.drop_column('hearing_version', '_area')
    op.drop_column('hearing', '_area')
    op.execute('DROP EXTENSION postgis')
