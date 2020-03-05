from flask import flash, redirect, request, current_app, url_for, render_template
from flask_mail import Message
from itsdangerous import TimedJSONWebSignatureSerializer

from . import auth
from ..forms import UserForgotPasswordForm
from ... import mail
from ...models import User


@auth.route('/request-password-reset', methods=['GET', 'POST'])
def request_password_reset():
    form = UserForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('Your email address doesnt exist', 'error')
            return redirect(request.url)
        else:
            try:
                msg = Message()
                msg.subject = 'Rest Password'
                msg.recipients = [user.email]
                serialize = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=1000)
                token = serialize.dumps({'user_id': user.id})
                url = url_for('auth.reset_password', token=token, _external=True)
                msg.body = f"""
                    Please Click On The Link TO Rest Your Rest Password
                    <a href='{url}'></a>
                """
                msg.sender = 'ISERVICE'
                mail.send(msg)
            except Exception as e:
                print(e)
                flash('An error occurred (check connection to the internet)', 'error')
                return redirect(request.url)
            else:
                flash('Message has been sent to your email to reset your password', 'error')
                return redirect(request.url)

    return render_template('auth/pages/request_password_reset.html', form=form, t='Forgot Password',
                           st='you can recover your password')
