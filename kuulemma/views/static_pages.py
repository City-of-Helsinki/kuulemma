from flask import Blueprint, render_template

static_pages = Blueprint(
    name='static_pages',
    import_name=__name__,
    url_prefix=''
)


@static_pages.route('/tietoa-palvelusta')
def service_info():
    return render_template('static_pages/service_info.html')


@static_pages.route('/hameentie')
def hameentie():
    return render_template('static_pages/hameentie.html')
