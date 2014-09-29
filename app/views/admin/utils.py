from flask.ext.admin.contrib import sqla
from flask.ext.login import current_user


class ModelView(sqla.ModelView):
    list_template = 'admin/model/list.html'
    edit_template = 'admin/model/edit.html'
    create_template = 'admin/model/create.html'
    create_excluded_columns = None
    edit_excluded_columns = None
    permissions = None
    requires_admin = False
    requires_super_user = False

    @property
    def _debug(self):
        k = 'FLASK_ADMIN_RAISE_EXCEPTIONS'
        if self.admin and (self.admin.app and
                           self.admin.app.config.get(k) is not None):
            return self.admin.app.debug and self.admin.app.config.get(k)
        return super(ModelView, self)._debug


class ProtectedModelView(ModelView):
    requires_admin = True

    def is_accessible(self):
        if not current_user.is_authenticated():
            return False
        if current_user.super_user:
            return True
        else:
            if self.requires_super_user:
                return False

        all_permissions = list(self.permissions or [])
        if self.requires_admin:
            all_permissions.append('admin')
        return all(current_user.has_role(permission) for permission
                   in all_permissions)
