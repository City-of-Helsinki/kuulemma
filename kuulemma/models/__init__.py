import sqlalchemy as sa

from .alternative import Alternative  # noqa
from .comment import Comment  # noqa
from .feedback import Feedback  # noqa
from .hearing import Hearing  # noqa
from .image import Image  # noqa
from .like import Like  # noqa
from .user import User  # noqa

# Force all mapper configuration listeners to fire.
# For example versioning listeners.
sa.orm.configure_mappers()
