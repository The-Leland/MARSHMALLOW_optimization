from flask import jsonify, request

from db import db
from models.product import Products
from models.category import Categories
from util.reflection import populate_object
from marshmallow import Schema, fields

class ProductSchema(Schema):
    product_id = fields.UUID()
    product_name = fields.String()
    description = fields.String()
    price = fields.Float()
    active = fields.Boolean()
    company_id = fields.UUID()

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


def add_product():
    post_data = request.form if request.form else request.get_json()

    new_product = Products(
        product_name="",
        description="",
        price=0,
        company_id=None
    )

    populate_object(new_product, post_data)

    db.session.add(new_product)
    db.session.commit()

    return jsonify({
        "message": "product created",
        "result": product_schema.dump(new_product)
    }), 201



def get_all_products():
    products = db.session.query(Products).all()

    return jsonify({
        "message": "products retrieved",
        "results": products_schema.dump(products)
    }), 200


def get_product_by_id(product_id):
    product = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not product:
        return jsonify({"message": "product not found"}), 404

    return jsonify({
        "message": "product retrieved",
        "result": product_schema.dump(product)
    }), 200



def update_product_by_id(product_id):
    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()
    post_data = request.form if request.form else request.get_json()

    if product_query:
        populate_object(product_query, post_data)
        db.session.commit()

        return jsonify({
            "message": "product updated",
            "results": product_schema.dump(product_query)
        }), 200

    return jsonify({"message": "unable to update record"}), 400



def delete_product_by_id(product_id):
    product = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not product:
        return jsonify({"message": "product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "product deleted"}), 200