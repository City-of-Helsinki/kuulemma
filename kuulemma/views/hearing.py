from flask import Blueprint, render_template

from ..models import Hearing

hearing = Blueprint(
    name='hearing',
    import_name=__name__,
    url_prefix='/kuulemiset'
)


@hearing.route('/<int:hearing_id>')
def show(hearing_id):
    hearing = Hearing.query.get_or_404(hearing_id)

    return render_template(
        'hearing/show.html',
        hearing=hearing
    )
