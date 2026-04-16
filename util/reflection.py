

from sqlalchemy import Table
from db import db

def reflect_table(table_name: str):
    return Table(table_name, db.metadata, autoload_with=db.engine)

def populate_object(obj, data):
    for field, value in data.items():
        if hasattr(obj, field):
            setattr(obj, field, value)
    return obj