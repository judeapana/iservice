import datetime
from enum import Enum
from sqlalchemy_utils import PasswordType, PhoneNumberType
from iservice import login_manager
from flask_login import UserMixin
from iservice.ext import db


@login_manager.user_loader
def load_user(pk):
    return User.query.get(pk)


class ActiveRecord:
    def save(self):
        db.session.add(self)
        db.session.commit()


class RoleType(Enum):
    ADMIN = 1
    USER = 2


class User(db.Model, ActiveRecord, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(PasswordType(max_length=255, schemes=['pbkdf2_sha512']), nullable=False)
    first_name = db.Column(db.String(255), nullable=False, info={'label': 'first name'})
    last_name = db.Column(db.String(255), nullable=False, info={'label': 'last name'})
    email = db.Column(db.String(255), nullable=False, unique=True)
    role = db.Column(db.Enum(RoleType), nullable=False)
    status = db.Column(db.Boolean)
    services = db.relationship('Service', backref=db.backref('user', lazy=True), secondary='user_service')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class UserService(db.Model, ActiveRecord):
    __tablename__ = 'user_service'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Service(db.Model, ActiveRecord):
    __searchable__ = ['title', 'location']
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    contact = db.Column(PhoneNumberType(region='GH'))
    charge = db.Column(db.Numeric(10, 2), nullable=False)
    img = db.Column(db.String(255), nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Category(db.Model, ActiveRecord):
    __searchable__ = ['name']
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text(255), nullable=True)
    charge_min = db.Column(db.Numeric(10, 2), nullable=False)
    charge_max = db.Column(db.Numeric(10, 2), nullable=False)
    service = db.relationship('Service', backref=db.backref('category', lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __str__(self):
        return f'{self.name} (Price GHS {self.charge_min} - GHS {self.charge_max} )'
