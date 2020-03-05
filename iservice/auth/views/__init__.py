from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

from . import register, forgot_pwd, reset_pwd, login,logout
