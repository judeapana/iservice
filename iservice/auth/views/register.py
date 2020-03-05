from flask import flash, redirect, request, render_template, url_for
from flask_login import current_user

from . import auth
from ..forms import UserRegisterForm
from ...models import User, RoleType


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You cant visit this page if you are logged in','info')
        return redirect(url_for('home.index'))
    form = UserRegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.status = True
        user.role = RoleType.USER
        user.save()
        flash('Your account has been created', 'success')
        return redirect(request.url)
    return render_template('auth/pages/register.html', form=form, t='Register Now', st='Become a Service Provider')
