def login_user(client, user):
    with client.session_transaction() as s:
        s['user_id'] = user.id
