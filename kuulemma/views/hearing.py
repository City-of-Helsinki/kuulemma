import csv
import io
from datetime import datetime

from flask import (
    abort,
    Blueprint,
    make_response,
    redirect,
    render_template,
    url_for
)
from flask.ext.login import current_user, login_required

from ..models import Hearing

hearing = Blueprint(
    name='hearing',
    import_name=__name__,
    url_prefix=''
)


# Redirects to the first hearing before the real index page is implemented.
@hearing.route('/kuulemiset')
def index():
    hearing = (
        Hearing.query
        .filter(Hearing.published)
        .first()
    )
    if not hearing:
        return redirect(url_for('frontpage.index'))

    return redirect(url_for('hearing.show', slug=hearing.slug))


@hearing.route('/<slug>')
def show(slug):
    hearing = (
        Hearing.query
        .filter(Hearing.slug == slug)
        .first()
    )

    if not hearing:
        return abort(404)

    if not (
        hearing.published or
        current_user.is_authenticated() and
        (current_user.is_official or current_user.is_admin)
    ):
        return abort(404)

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

    HAMEENTIE_HEARING_ID = 11
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


@hearing.route('/<slug>/raportti.csv')
def report(slug):
    hearing = (
        Hearing.query
        .filter(Hearing.slug == slug)
        .first()
    )

    if not (hearing and hearing.published):
        return abort(404)

    # Format csv string.
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
    filename = '{slug}_raportti_{date}'.format(
        slug=hearing.slug,
        date=datetime.utcnow().strftime('%d-%m-%Y')
    )

    headers = [
        'Otsikko',
        'Viittaa',
        'Kirjoittaja',
        'Saapunut',
        'Kannatettu',
        'Mielipide',
    ]
    writer.writerow(headers)

    for comment in hearing.comments_for_report:
        writer.writerow(comment.csv_value_array)

    csv_as_string = output.getvalue()
    response = make_response(csv_as_string)
    response.headers['Content-Disposition'] = (
        'attachment; filename={filename}.csv'.format(filename=filename)
    )
    return response
