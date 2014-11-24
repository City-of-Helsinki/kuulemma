from flask import Blueprint, render_template

from kuulemma.extensions import db
from kuulemma.models import Hearing

frontpage = Blueprint(
    name='frontpage',
    import_name=__name__,
    url_prefix=''
)


@frontpage.route('/')
def index():
    featured_hearing = (
        Hearing.query
        .filter(Hearing.published)
        .order_by(db.desc(Hearing.closes_at))
        .limit(1)
        .first()
    )

    latest_hearings = (
        Hearing.query
        .filter(Hearing.published)
        .order_by(db.desc(Hearing.opens_at))
        .limit(5)
    )

    return render_template(
        'frontpage/index.html',
        featured_hearing=featured_hearing,
        latest_hearings=latest_hearings,
    )
