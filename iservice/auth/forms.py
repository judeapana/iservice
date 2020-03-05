from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms_alchemy import ModelForm
from wtforms_components import EmailField

from iservice.models import User


class UserRegisterForm(ModelForm, FlaskForm):
    class Meta:
        model = User
        only = ['username', 'password', 'first_name', 'last_name', 'email']


class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class UserForgotPasswordForm(FlaskForm):
    email = EmailField('Email Address', validators=[InputRequired(), Email()])


class UserResetPasswordForm(ModelForm, FlaskForm):
    password = PasswordField('Password', validators=[InputRequired()])
    cpassword = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
