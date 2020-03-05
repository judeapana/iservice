from flask import request, url_for, redirect, render_template
from sqlalchemy import or_

from . import home
from ..forms import SearchServiceForm
from ...models import Category, Service


@home.route('/search/', methods=['GET', 'POST'])
def search():
    cat_id = request.args.get('cat_id', type=int)
    if cat_id:
        cats = Category.query.get(cat_id)
        return render_template('home/pages/search.html', cats=cats, t='Search results', st='Search any category')
    return redirect(url_for('home.index'))


@home.route('/search/service', methods=['GET', 'POST'])
def search_service():
    form = SearchServiceForm()
    location = request.args.get('location', type=str)
    title = request.args.get('title', type=str)
    page = request.args.get('page', type=int)
    if not (location or title):
        return redirect(url_for('home.index'))
    ser = Service.query.filter(or_(Service.location.like(location), Service.title.like(title))).paginate(page=page,
                                                                                                         per_page=10)
    return render_template('home/pages/search_service.html', services=ser, form=form, l=location, tt=title,p=page)


@home.route('/search/service/all', methods=['GET', 'POST'])
def search_all():
    form = SearchServiceForm()
    page = request.args.get('page', type=int)
    ser = Service.query.paginate(page=page, per_page=10)
    return render_template('home/pages/search_all.html', services=ser, form=form)
