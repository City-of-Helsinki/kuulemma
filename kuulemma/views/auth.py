# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.ext.login import current_user, login_user, logout_user

from kuulemma.extensions import db, login_manager
from kuulemma.forms import LoginForm
from kuulemma.models import User

auth = Blueprint(
    name='auth',
    import_name=__name__,
    url_prefix=''
)


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


login_manager.login_message = ('Kirjaudu sisään nähdäksesi tämän sivun.')
login_manager.login_view = 'auth.login'


@auth.after_app_request
def update_user_last_seen(response):
    """
    Keep up-to-date when the user has been last seen at.

    Writes user's last seen at status to the database only every 10 minutes in
    order to keep the throughput high.
    """
    if current_user.is_authenticated() and 'online' not in request.cookies:
        if current_user.date_joined is None:
            current_user.date_joined = datetime.utcnow()
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

        expires = datetime.utcnow() + timedelta(minutes=10)
        response.set_cookie('online', '1', expires=expires)
    return response


@auth.route('/kirjaudu-sisaan', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('frontpage.index'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=True)
            flash('Olet nyt kirjautuneena sisään.', 'success')
            return redirect(
                request.args.get('next') or
                url_for('frontpage.index')
            )
        else:
            flash(
                'Syöttämäsi sähköpostiosoite ja salasana eivät täsmää.',
                'danger'
            )

    return render_template('auth/login.html', form=form)


@auth.route('/kirjaudu-ulos')
def logout():
    logout_user()
    return redirect(url_for('frontpage.index'))
