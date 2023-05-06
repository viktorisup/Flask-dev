from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, LoginManager, login_required, login_user, current_user
from werkzeug.security import check_password_hash

from blog.forms.auth import UserAuthForm
from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))


__all__ = [
    'load_user',
    'auth',
]


@auth.route('/login', methods=['POST', 'GET'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user_bp.profile', pk=current_user.id))
    form = UserAuthForm(request.form)
    errors = []

    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user is None:
            errors.append("user with such email doesn't exist")
            return render_template("auth/login.html", form=form, errors=errors)
        if not check_password_hash(user.password, request.form.get('password')):
            errors.append("invalid email or password")
            return render_template("auth/login.html", form=form, errors=errors)
        login_user(user)
        return redirect(url_for('user_bp.profile', pk=current_user.id))
    return render_template(
        'auth/login.html',
        form=form,
        errors=errors,
    )


@auth.route('/logout', endpoint='logout')
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route('/secret')
@login_required
def secret_view():
    return 'Super secret data'
