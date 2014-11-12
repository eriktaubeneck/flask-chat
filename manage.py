from datetime import datetime
from flask.ext.script import Manager
from flask.ext.security.utils import encrypt_password
from foundry import SQLAlchemyFoundry, Mold
from app.factory import create_app
from app.models import db
from app.models.user import User, Role

app = create_app()

manager = Manager(app)

user_converters = {
    'confirmed_at': lambda s: datetime.strptime(s, '%Y-%m-%d'),
    'password': lambda s: encrypt_password(s),
}

foundry = SQLAlchemyFoundry(
    db.session,
    [('roles.yml', Role),
     Mold('users.yml', User, str_converters=user_converters), ],
    path='foundry_data',
)


@manager.shell
def _make_context():
    return {'db': db,
            'fixtures': foundry}


@manager.command
def drop_and_create_db():
    db.drop_all()
    db.create_all()


@manager.command
def populate_db():
    foundry.load()

if __name__ == '__main__':
    manager.run()
