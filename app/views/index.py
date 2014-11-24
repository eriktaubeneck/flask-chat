from flask import render_template, Blueprint


index_bp = Blueprint('index', __name__, url_prefix='/')


@index_bp.route('/', methods=('GET',))
def index(**kwargs):
    return render_template('index.html', **kwargs)
