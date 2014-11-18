from flask import Blueprint, render_template

static_pages = Blueprint(
    name='static_pages',
    import_name=__name__,
    url_prefix=''
)


@static_pages.route('/hameentie')
def hameentie():
    return render_template('static_pages/hameentie.html')
