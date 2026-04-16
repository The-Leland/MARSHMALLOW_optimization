from db import db
from models.product import Products
from util.reflection import populate_object


def add_product(data):
    new_product = Products(
        name="",
        description="",
        price=0,
        active=True,
        company_id=None
    )

    populate_object(new_product, data)

    db.session.add(new_product)
    db.session.commit()

    return new_product


def get_all_products():
    return db.session.query(Products).all()


def get_product_by_id(product_id):
    product = db.session.query(Products).filter(Products.product_id == product_id).first()
    return product


def update_product_by_id(product_id, data):
    product = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not product:
        return None

    populate_object(product, data)
    db.session.commit()

    return product


def delete_product_by_id(product_id):
    product = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not product:
        return None

    db.session.delete(product)
    db.session.commit()

    return product


def get_active_products():
    return db.session.query(Products).filter(Products.active == True).all()


def get_products_by_company(company_id):
    return db.session.query(Products).filter(Products.company_id == company_id).all()
