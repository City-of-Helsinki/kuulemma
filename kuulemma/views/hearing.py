from flask import Blueprint, redirect, render_template, url_for
from sqlalchemy import desc

from ..models import Comment, Hearing

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

    latest_comments = (
        Comment.query
        .filter(Comment.hearing == hearing)
        .order_by(desc(Comment.created_at))
    )
    # TODO: Change this into number of likes when likes are implemented.
    popular_comments = (
        Comment.query
        .filter(Comment.hearing == hearing)
    )

    commentable_sections_string = hearing.get_commentable_sections_string()

    return render_template(
        'hearing/show.html',
        hearing=hearing,
        latest_comments=latest_comments,
        popular_comments=popular_comments,
        commentable_sections_string=commentable_sections_string
    )
