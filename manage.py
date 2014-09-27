from flask.ext.script import Manager
from app.factory import create_app
from app.models import db

app = create_app()

manager = Manager(app)

@manager.shell
def _make_context():
    return {'db': db}

@manager.command
def drop_and_create_db():
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
