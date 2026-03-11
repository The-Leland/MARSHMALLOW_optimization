from flask import jsonify, request

from db import db
from models.warranty import Warranties
from util.reflection import populate_object
from marshmallow import Schema, fields

class WarrantySchema(Schema):
    warranty_id = fields.UUID()
    product_id = fields.UUID()
    duration_months = fields.Integer()
    details = fields.String()

warranty_schema = WarrantySchema()
warranties_schema = WarrantySchema(many=True)


def add_warranty():
    post_data = request.form if request.form else request.get_json()

    new_warranty = Warranties(
        warranty_length=0,
        warranty_description="",
        product_id=None
    )

    populate_object(new_warranty, post_data)

    db.session.add(new_warranty)
    db.session.commit()

    return jsonify({
        "message": "warranty created",
        "result": warranty_schema.dump(new_warranty)
    }), 201



def get_all_warranties():
    warranties = db.session.query(Warranties).all()

    return jsonify({
        "message": "warranties retrieved",
        "results": warranties_schema.dump(warranties)
    }), 200


def get_warranty_by_id(warranty_id):
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    return jsonify({
        "message": "warranty retrieved",
        "result": warranty_schema.dump(warranty)
    }), 200



def update_warranty_by_id(warranty_id):
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()
    post_data = request.form if request.form else request.get_json()

    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    populate_object(warranty, post_data)
    db.session.commit()

    return jsonify({
        "message": "warranty updated",
        "result": warranty_schema.dump(warranty)
    }), 200



def delete_warranty(warranty_id):
    warranty = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    db.session.delete(warranty)
    db.session.commit()

    return jsonify({"message": "warranty deleted"}), 200