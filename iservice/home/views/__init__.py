from flask import Blueprint

home = Blueprint('home', __name__, template_folder='templates', url_prefix='/')

from . import index, category, search, service
