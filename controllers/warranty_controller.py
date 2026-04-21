
from flask import jsonify, request
from db import db
from models import Warranties, warranty_schema, warranties_schema
from util.reflection import populate_object


def add_warranty():
    data = request.form if request.form else request.get_json()

    new_warranty = Warranties(
        product_id=data.get("product_id"),
        warranty_months=data.get("warranty_months")
    )

    try:
        db.session.add(new_warranty)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create warranty"}), 400

    return jsonify({
        "message": "warranty created",
        "result": warranty_schema.dump(new_warranty)
    }), 201


def get_all_warranties():
    warranties = Warranties.query.all()
    return jsonify({
        "message": "warranties retrieved",
        "results": warranties_schema.dump(warranties)
    }), 200


def get_warranty_by_id(warranty_id):
    warranty = Warranties.query.filter_by(warranty_id=warranty_id).first()

    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    return jsonify({
        "message": "warranty retrieved",
        "result": warranty_schema.dump(warranty)
    }), 200


def update_warranty_by_id(warranty_id):
    warranty = Warranties.query.filter_by(warranty_id=warranty_id).first()

    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    data = request.form if request.form else request.get_json()
    populate_object(warranty, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update warranty"}), 400

    return jsonify({
        "message": "warranty updated",
        "result": warranty_schema.dump(warranty)
    }), 200


def delete_warranty_by_id(warranty_id):
    warranty = Warranties.query.filter_by(warranty_id=warranty_id).first()

    if not warranty:
        return jsonify({"message": "warranty not found"}), 404

    try:
        db.session.delete(warranty)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete warranty"}), 400

    return jsonify({"message": "warranty deleted"}), 200

