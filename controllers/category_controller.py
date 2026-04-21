
from models.category import Categories
from util.reflection import populate_object
from db import db


def add_category(data):
    new_category = Categories(
        category_name="",
        active=True
    )

    populate_object(new_category, data)

    db.session.add(new_category)
    db.session.commit()
    
    return new_category


def get_all_categories():
    return db.session.query(Categories).all()


def get_category_by_id(category_id):
    return db.session.query(Categories).filter_by(category_id=category_id).first()


def update_category_by_id(category_id, data):
    category = db.session.query(Categories).filter_by(category_id=category_id).first()

    if not category:
        return None

    populate_object(category, data)
    db.session.commit()

    return category


def delete_category_by_id(category_id):
    category = db.session.query(Categories).filter_by(category_id=category_id).first()

    if not category:
        return None

    db.session.delete(category)
    db.session.commit()

    return category
