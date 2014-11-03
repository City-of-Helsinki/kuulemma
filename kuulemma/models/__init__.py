import sqlalchemy as sa

from .comment import Comment  # noqa
from .hearing import Hearing  # noqa
from .hearing_section import HearingSection  # noqa
from .user import User  # noqa

# Force all mapper configuration listeners to fire.
# For example versioning listeners.
sa.orm.configure_mappers()
