from flask import render_template, redirect, request, flash, url_for

from . import home
from ..forms import SearchServiceForm, CategoryForm
from ... import db
from ...models import Category
from ...utils import upload_image


@home.route('/category', methods=['GET', 'POST'])
def category():
    form = SearchServiceForm()
    cats = Category.query.all()
    return render_template('home/pages/category.html', cats=cats, t='All Categories',
                           st='find all categories of services', form=form)


@home.route('/category/create', methods=['GET', 'POST'])
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        cat = Category()
        form.populate_obj(cat)
        cat.save()
        flash('Category has been created', 'success')
        return redirect(request.url)
    return render_template('home/pages/create_category.html', form=form, t='Create New Category',
                           st='Creating a new Category for services')


@home.route('/category/update/<int:pk>', methods=['GET', 'POST'])
def update_category(pk):
    cat = Category.query.get_or_404(pk)
    form = CategoryForm(obj=cat)
    if form.validate_on_submit():
        form.populate_obj(cat)
        cat.save()
        flash('Category has been updated', 'success')
        return redirect(url_for('home.category'))
    return render_template('home/pages/update_category.html', form=form, t='Update Category',
                           st='Update your category (Admin Only)', pk=pk)


@home.route('/category/delete/<int:pk>', methods=['GET', 'POST'])
def delete_category(pk):
    cat = Category.query.get_or_404(pk)
    db.session.delete(cat)
    db.session.commit()
    flash('Category has been deleted', 'success')
    return redirect(url_for('home.category'))
