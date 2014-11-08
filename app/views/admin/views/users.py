from app.views.admin.utils import ProtectedModelView


class UserModelView(ProtectedModelView):
    can_create = False
    can_delete = False

    column_list = ('fullname', 'email', 'active', 'confirmed_at',)

    column_searchable_list = ('fullname', 'email',)
    column_filters = ('fullname', 'email',)

    form_columns = ('fullname', 'email', 'active', 'confirmed_at',)

    form_edit_rules = ('fullname', 'email', 'active', 'confirmed_at',)
