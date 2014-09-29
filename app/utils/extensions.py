from flask import current_app
from werkzeug import LocalProxy


def get_extension(name, app=None):
    if not app:
        app = current_app
    return LocalProxy(lambda: app.extensions[name])
