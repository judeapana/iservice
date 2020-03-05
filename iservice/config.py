class BaseConfig:
    DEBUG = True
    ENV = 'development'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'androapana@gmail.com'
    MAIL_PORT = 465
    MAIL_PASSWORD = 'apana1jude1'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    SECRET_KEY = '75c183bcc5c0d56c9865bda264f15382668776fee4a6ba284b91605a0c495bf088b3dd7e7517c0321072fc33'
    MAIL_SENDER = 'androapana@gmail.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://localhost/iservice2'
    WHOOSH_BASE = 'whoosh'


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
