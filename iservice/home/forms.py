from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import FileField
from wtforms.validators import InputRequired, Optional
from wtforms_alchemy import ModelForm, QuerySelectField
from iservice.models import Service, Category


class ServiceForm(ModelForm, FlaskForm):
    class Meta:
        model = Service

    category = QuerySelectField('Category', validators=[InputRequired()], query_factory=lambda: Category.query.all())
    img = FileField('Image', validators=[FileAllowed(['png', 'jpg', 'jpeg', 'gif']), Optional()])


class SearchServiceForm(ModelForm):
    location = QuerySelectField('Location', validators=[InputRequired()], query_factory=lambda: Service.query,
                                get_label='location', get_pk=lambda x: x.location)
    title = QuerySelectField('Title', validators=[InputRequired()], query_factory=lambda: Service.query,
                             get_label='title', get_pk=lambda x: x.title)
    category = QuerySelectField('Category', validators=[InputRequired()], query_factory=lambda: Category.query)


class CategoryForm(ModelForm, FlaskForm):
    class Meta:
        model = Category
        only = ['name', 'description', 'charge_min', 'charge_max']
