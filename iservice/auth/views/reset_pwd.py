from flask import current_app, flash, redirect, url_for, render_template
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature

from . import auth
from ..forms import UserResetPasswordForm
from ...models import User


@auth.route('/rest-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        serialise = TimedJSONWebSignatureSerializer(current_app.secret_key)
        d_serial = serialise.loads(token)
        if not d_serial['user_id']:
            flash('Rest password token has expired or is invalid', 'error')
            return redirect(url_for('auth.request_password_reset'))
        else:
            user = User.query.get(int(d_serial['user_id']))
    except BadSignature:
        flash('Rest password token has expired or is invalid', 'error')
        return redirect(url_for('auth.request_password_reset'))

    form = UserResetPasswordForm()
    if form.validate_on_submit():
        form.populate_obj(user)
        user.save()
        flash('Password has been successfully saved', 'success')
        return redirect(url_for('auth.index'))
    return render_template('auth/pages/reset_password.html', form=form, token=token, t='Rest Password',
                           st='change your password')
