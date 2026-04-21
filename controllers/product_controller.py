from flask import jsonify, request
from db import db
from models import Products, product_schema, products_schema
from util.reflection import populate_object


def add_product():
    data = request.form if request.form else request.get_json()

    new_product = Products(
        product_name=data.get("product_name"),
        description=data.get("description"),
        price=data.get("price"),
        company_id=data.get("company_id"),
        active=data.get("active", True)
    )

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create product"}), 400

    return jsonify({
        "message": "product created",
        "result": product_schema.dump(new_product)
    }), 201


def get_all_products():
    products = Products.query.all()
    return jsonify({
        "message": "products retrieved",
        "results": products_schema.dump(products)
    }), 200


def get_product_by_id(product_id):
    product = Products.query.filter_by(product_id=product_id).first()

    if not product:
        return jsonify({"message": "product not found"}), 404

    return jsonify({
        "message": "product retrieved",
        "result": product_schema.dump(product)
    }), 200


def update_product_by_id(product_id):
    product = Products.query.filter_by(product_id=product_id).first()

    if not product:
        return jsonify({"message": "product not found"}), 404

    data = request.form if request.form else request.get_json()
    populate_object(product, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update product"}), 400

    return jsonify({
        "message": "product updated",
        "result": product_schema.dump(product)
    }), 200


def delete_product_by_id(product_id):
    product = Products.query.filter_by(product_id=product_id).first()

    if not product:
        return jsonify({"message": "product not found"}), 404

    try:
        db.session.delete(product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete product"}), 400

    return jsonify({"message": "product deleted"}), 200


def get_active_products():
    products = Products.query.filter_by(active=True).all()
    return jsonify({
        "message": "active products retrieved",
        "results": products_schema.dump(products)
    }), 200


def get_products_by_company(company_id):
    products = Products.query.filter_by(company_id=company_id).all()
    return jsonify({
        "message": "products retrieved for company",
        "results": products_schema.dump(products)
    }), 200
