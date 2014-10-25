from flask import Blueprint, redirect, render_template, url_for

from ..models import Hearing

hearing = Blueprint(
    name='hearing',
    import_name=__name__,
    url_prefix='/kuulemiset'
)


@hearing.route('/<int:hearing_id>-<slug>')
def show(hearing_id, slug):
    hearing = Hearing.query.get_or_404(hearing_id)

    if hearing.slug != slug:
        return redirect(
            url_for('hearing.show', hearing_id=hearing_id, slug=hearing.slug)
        )

    return render_template(
        'hearing/show.html',
        hearing=hearing
    )
