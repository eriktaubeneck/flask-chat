from ordbok.flask_helper import Flask
from app import security
from app.utils.processors import register_processors
from app.models import db
from app.models.user import user_datastore
from app.views.index import index_bp


def create_app(config=None, environment=None):
    app = Flask(__name__)
    app.config['ENVIRONMENT'] = environment
    app.config.load()
    app.config.update(config or {})
    if not (app.config['ENVIRONMENT'] == 'development' or
            app.config['TESTING']):
        app.config['SERVER_NAME'] = app.config['SITE_URL']

    security.init_app(app, user_datastore)
    db.init_app(app)
    app.register_blueprint(index_bp)

    register_processors(app)

    return app
