# -*- coding: utf-8 -*-
# Kuulemma
# Copyright (C) 2014, Fast Monkeys Oy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
