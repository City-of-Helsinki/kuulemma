from flask import Blueprint, render_template

frontpage = Blueprint(
    name='frontpage',
    import_name=__name__,
    url_prefix=''
)


@frontpage.route('/')
def index():
    return render_template('frontpage/index.html')
