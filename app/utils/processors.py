from flask.ext.security import current_user, LoginForm
from app.forms import RegisterForm


def user_context_processor():
    if current_user.is_authenticated():
        user = current_user._get_current_object()
    else:
        user = None
    return {
        'user': user,
        'login_user_form': LoginForm(),
        'register_form': RegisterForm(),
    }


def register_processors(app):
    app.context_processor(user_context_processor)

    security = app.extensions['security']

    @security.login_context_processor
    def login_context_processor():
        return {'show_modal': 'login-signup'}
