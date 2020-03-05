from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
