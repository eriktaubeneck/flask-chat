import redis
from ordbok.flask_helper import Flask
from app import sockets, chat
from app.views.index import index_bp
from app.views.chat import register_chat_routes


def create_app(config=None, environment=None):
    app = Flask(__name__)
    app.config['ENVIRONMENT'] = environment
    app.config.load()
    app.config.update(config or {})
    if not (app.config['ENVIRONMENT'] == 'development' or
            app.config['TESTING']):
        app.config['SERVER_NAME'] = app.config['SITE_URL']

    sockets.init_app(app)
    app.redis = redis.from_url(app.config['REDIS_URL'])

    chat.init_app(app)
    chat.start()
    app.register_blueprint(index_bp)
    register_chat_routes(app, sockets)

    return app
