"""Add map_coordenates and area to hearings"""

# revision identifiers, used by Alembic.
revision = '3aa8d3b65ff'
down_revision = '3724320b21a'

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
        'hearing',
        sa.Column(
            '_map_coordinates',
            ga.Geometry(geometry_type='POINT'),
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
    op.add_column(
        'hearing_version',
        sa.Column(
            '_map_coordinates',
            ga.Geometry(geometry_type='POINT'),
            autoincrement=False,
            nullable=True
        )
    )


def downgrade():
    op.drop_column('hearing_version', '_map_coordinates')
    op.drop_column('hearing_version', '_area')
    op.drop_column('hearing', '_map_coordinates')
    op.drop_column('hearing', '_area')
    op.execute('DROP EXTENSION postgis')
