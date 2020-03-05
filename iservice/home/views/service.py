from flask import render_template, flash, redirect, request, abort, url_for
from flask_login import login_required, current_user

from . import home
from ..forms import ServiceForm
from ... import db
from ...models import Service, User
from ...utils import upload_image


@home.route('/service', methods=['GET', 'POST'])
@login_required
def service():
    return render_template('home/pages/service.html', t='Service Post', st='All Service Post')


@home.route('/service/create', methods=['GET', 'POST'])
@login_required
def create_service():
    form = ServiceForm()
    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        se = Service()
        form.populate_obj(se)
        se.img = upload_image(form.img.data)
        user.services.append(se)
        user.save()
        flash('Your service has been created', 'success')
        return redirect(request.url)
    return render_template('home/pages/create_service.html', t='Create Service', st='post your service', form=form)


@home.route('/service/update/<int:pk>', methods=['GET', 'POST'])
@login_required
def update_service(pk):
    se = Service.query.filter_by(id=pk).first_or_404()
    if se.user[0].id != current_user.id:
        abort(403)
    form = ServiceForm(obj=se)
    if form.validate_on_submit():
        se.title = form.title.data
        se.description = form.description.data
        se.location = form.location.data
        se.contact = form.contact.data
        se.charge = form.charge.data
        se.cat_id = form.category.data.id
        if form.img.data:
            se.img = upload_image(form.img.data)
        se.save()
        flash('Service has been updated', 'success')
        return redirect(url_for('home.service'))
    return render_template('home/pages/update_service.html', form=form, t='Edit Service Post', pk=pk)


@home.route('/service/delete/<int:pk>', methods=['POST', 'GET'])
@login_required
def delete_service(pk):
    se = Service.query.get_or_404(pk)
    db.session.delete(se)
    db.session.commit()
    return redirect(url_for('home.service'))
