# flask-sqlalchemy
# This file is to solve the problem of circular references
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_caching import Cache

db = SQLAlchemy()
mail = Mail()
cache = Cache(
    config={'CACHE_TYPE': 'simple'}
)


def init_exts(app):
    db.init_app(app)
    mail.init_app(app)
    cache.init_app(app)