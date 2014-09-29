from flask import (Blueprint, render_template, current_app, redirect, request,
                   flash)
from flask.ext.security import current_user, login_user

from app.utils.extensions import get_extension
from app.forms import RegisterForm

index_bp = Blueprint('index', __name__, url_prefix='/')


class IndexView:
    @classmethod
    def index(cls, **kwargs):
        return render_template('index.html', **kwargs)

    @classmethod
    def register(cls, login_failed=False, **kwargs):
        if current_user.is_authenticated():
            return redirect(request.referrer or '/')

        form = RegisterForm()

        ds = get_extension('security', app=current_app).datastore
        if form.validate_on_submit():
            user = ds.create_user(
                fullname=form.fullname.data,
                email=form.email.data,
                password=form.password.data)
            ds.commit()

            login_user(user)
            ds.commit()
            flash('Account created successfully', 'info')
            return cls.index(show_modal='profile')

        if form.errors:
            show_modal = 'login-signup'
        else:
            show_modal = None

        return cls.index(
            register_form=form,
            show_modal=show_modal)

    @classmethod
    def register_routes(cls, index_bp):
        index_bp.add_url_rule(
            '', 'index', view_func=cls.index, methods=["GET"])
        index_bp.add_url_rule(
            'register', 'register', view_func=cls.register,
            methods=['POST', 'GET'])

IndexView.register_routes(index_bp)
