from flask.ext.script import Manager
from app.factory import create_app

app = create_app()

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
