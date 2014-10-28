import sqlalchemy as sa

from .hearing import Hearing  # noqa
from .hearing_section import HearingSection  # noqa

# Force all mapper configuration listeners to fire.
# For example versioning listeners.
sa.orm.configure_mappers()
