from flask import render_template, request

from . import home
from ..forms import SearchServiceForm
from ... import Service


@home.route('/', methods=['GET', 'POST'])
def index():
    form = SearchServiceForm()
    page = request.args.get('page', type=int)
    se = Service.query.paginate(page=page, per_page=10)
    return render_template('home/pages/index.html', t='IService', services=se, form=form,p=page)
