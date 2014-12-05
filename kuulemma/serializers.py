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

from hashlib import sha512

from flask import current_app
from itsdangerous import URLSafeSerializer
from werkzeug.local import LocalProxy

account_activation_serializer = LocalProxy(
    lambda: URLSafeSerializer(
        secret_key=current_app.config['SECRET_KEY'],
        salt='active_account',
        signer_kwargs={
            'key_derivation': 'hmac',
            'digest_method': sha512
        }
    )
)
