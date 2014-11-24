from flask import abort, Blueprint, redirect, render_template, url_for
from flask.ext.login import current_user, login_required

from ..models import Hearing

hearing = Blueprint(
    name='hearing',
    import_name=__name__,
    url_prefix='/kuulemiset'
)


# Redirects to the first hearing before the real index page is implemented.
@hearing.route('')
def index():
    hearing = (
        Hearing.query
        .filter(Hearing.published)
        .first()
    )
    if not hearing:
        return redirect(url_for('frontpage.index'))

    return redirect(url_for(
        'hearing.show',
        hearing_id=hearing.id,
        slug=hearing.slug
    ))


@hearing.route('/<int:hearing_id>-<slug>')
def show(hearing_id, slug):
    hearing = Hearing.query.get_or_404(hearing_id)

    if not (
        hearing.published or
        current_user.is_authenticated() and
        (current_user.is_official or current_user.is_admin)
    ):
        return abort(404)

    if hearing.slug != slug:
        return redirect(
            url_for('hearing.show', hearing_id=hearing_id, slug=hearing.slug)
        )

    commentable_sections_string = hearing.get_commentable_sections_string()

    return render_template(
        'hearing/show.html',
        hearing=hearing,
        commentable_sections_string=commentable_sections_string,
        hearing_page_active=True
    )


# This route is only for demo and preview purposes.
@hearing.route('/hameentie-ennakko')
@login_required
def hameentie():
    if not (current_user.is_official or current_user.is_admin):
        return abort(404)

    HAMEENTIE_HEARING_ID = 1
    hearing = Hearing.query.get(HAMEENTIE_HEARING_ID)

    if not hearing:
        return abort(404)

    commentable_sections_string = hearing.get_commentable_sections_string()

    return render_template(
        'hearing/show.html',
        hearing=hearing,
        commentable_sections_string=commentable_sections_string,
        hearing_page_active=True
    )
