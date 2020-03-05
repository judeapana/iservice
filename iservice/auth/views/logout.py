from flask import flash, url_for
from flask_login import login_required, logout_user
from werkzeug.utils import redirect

from . import auth


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out', 'success')
    return redirect(url_for('auth.index'))
