from flask import Flask
from iservice.config import DevelopmentConfig
from iservice.ext import mail, db, login_manager, migrate
from .models import Category, Service
import flask_whooshalchemyplus as wa


def create_app(configuration=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(configuration)
    db.init_app(app)
    wa.whoosh_index(app, Category)
    wa.whoosh_index(app, Service)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.index'
    app.register_blueprint(auth)
    app.register_blueprint(home)
    migrate.init_app(app, db)
    return app


from iservice.auth.views import auth
from iservice.home.views import home
