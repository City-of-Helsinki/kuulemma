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
    latest_hearings = (
        Hearing.query
        .order_by(db.desc(Hearing.opens_at))
        .limit(5)
    )

    return render_template(
        'frontpage/index.html',
        latest_hearings=latest_hearings
    )
