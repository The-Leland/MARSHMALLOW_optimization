
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__all__ = ('db', 'init_db')

db = SQLAlchemy()

def init_db(app):
    if isinstance(app, Flask):
        db.init_app(app)
    else:
        raise ValueError('init_db requires a Flask app instance')
    