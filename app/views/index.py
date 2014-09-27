from flask import Blueprint, render_template
from flask.ext.security import login_required

index_bp = Blueprint('index', __name__, url_prefix='/')


class IndexView:
    @classmethod
    def index(cls, **kwargs):
        return render_template('index.html')

    @classmethod
    def register(cls, index_bp):
        index_bp.add_url_rule(
            '/', 'index', view_func=cls.index, methods=["GET"])

IndexView.register(index_bp)
