from flask import flash, redirect, request, url_for, render_template
from flask_login import login_user, current_user
from . import auth
from ..forms import UserLoginForm
from ...models import User, RoleType


@auth.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        flash('You cant visit this page if you are logged in','info')
        return redirect(url_for('home.index'))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash('Incorrect username or password', 'error')
            return redirect(request.url)
        else:
            if not user.password == form.password.data:
                flash('Incorrect username or password', 'error')
                return redirect(request.url)
            else:
                if user.role == RoleType.USER:
                    login_user(user)
                    flash('You have successfully logged in', 'success')
                    return redirect(url_for('home.service'))
                elif user.role == RoleType.ADMIN:
                    login_user(user)
                    flash('You have successfully logged in as admin', 'success')
                    return redirect(url_for('home.create_service'))
                else:
                    flash('Sorry a problem occurred', 'error')
                    return redirect(url_for('home.create_service'))
    return render_template('auth/pages/index.html', form=form, t='Login Now', st='Manage your own services')
