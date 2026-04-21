
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

__all__ = ('db', 'init_db')

db = SQLAlchemy()
ma = Marshmallow()

def init_db(app):
    if isinstance(app, Flask):
        db.init_app(app)
        ma.init_app(app)
    else:
        raise ValueError('init_db requires a Flask app instance')
    