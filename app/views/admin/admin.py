from flask.ext.admin import Admin
from flask.ext.login import current_user
from app.models import db
from app.models.user import User
from app.views.admin.views.users import UserModelView


admin = Admin(url='/admin',
              template_mode='bootstrap3',
              base_template='admin/base.html',
              name='Mirror Park')


def is_accessible():
    if not current_user.is_authenticated():
        return False
    return current_user.has_role('admin')

admin.index_view.is_accessible = is_accessible
admin.add_view(UserModelView(User, db.session, name="User"))
