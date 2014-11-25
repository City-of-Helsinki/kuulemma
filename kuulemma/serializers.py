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
