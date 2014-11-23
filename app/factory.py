import redis
from ordbok.flask_helper import Flask
from app import security, sockets, chat
from app.utils.processors import register_processors
from app.models import db
from app.models.user import user_datastore
from app.views.index import index_bp
from app.views.admin import admin
from app.views.chat import register_chat_routes


def create_app(config=None, environment=None):
    app = Flask(__name__)
    app.config['ENVIRONMENT'] = environment
    app.config.load()
    app.config.update(config or {})
    if not (app.config['ENVIRONMENT'] == 'development' or
            app.config['TESTING']):
        app.config['SERVER_NAME'] = app.config['SITE_URL']

    security.init_app(app, user_datastore)
    sockets.init_app(app)
    app.redis = redis.from_url(app.config['REDIS_URL'])

    db.init_app(app)
    admin.init_app(app)
    chat.init_app(app)
    chat.start()
    app.register_blueprint(index_bp)
    register_chat_routes(app, sockets)

    register_processors(app)

    return app
