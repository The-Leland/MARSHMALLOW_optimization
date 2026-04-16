
from db import db
from models.warranty import Warranties
from util.reflection import populate_object


def add_warranty(data):
    new_warranty = Warranties(
        warranty_length=0,
        warranty_description="",
        product_id=None
    )

    populate_object(new_warranty, data)

    db.session.add(new_warranty)
    db.session.commit()

    return new_warranty


def get_all_warranties():
    return db.session.query(Warranties).all()


def get_warranty_by_id(warranty_id):
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()
    return warranty


def update_warranty_by_id(warranty_id, data):
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    if not warranty:
        return None

    populate_object(warranty, data)
    db.session.commit()

    return warranty


def delete_warranty_by_id(warranty_id):
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    if not warranty:
        return None

    db.session.delete(warranty)
    db.session.commit()

    return warranty

