from flask import jsonify, request
from db import db
from models import ProductsCategoriesXref, product_category_schema, product_categories_schema


def add_product_category():
    data = request.form if request.form else request.get_json()

    new_link = ProductsCategoriesXref(
        product_id=data.get("product_id"),
        category_id=data.get("category_id")
    )

    try:
        db.session.add(new_link)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create product-category link"}), 400

    return jsonify({
        "message": "product category created",
        "result": product_category_schema.dump(new_link)
    }), 201


def get_all_product_categories():
    links = ProductsCategoriesXref.query.all()
    return jsonify({
        "message": "product categories retrieved",
        "results": product_categories_schema.dump(links)
    }), 200


def get_categories_for_product(product_id):
    links = ProductsCategoriesXref.query.filter_by(product_id=product_id).all()

    results = [
        {"product_id": link.product_id, "category_id": link.category_id}
        for link in links
    ]

    return jsonify({
        "message": "categories retrieved for product",
        "results": results
    }), 200


def delete_product_category():
    data = request.form if request.form else request.get_json()

    link = ProductsCategoriesXref.query.filter_by(
        product_id=data.get("product_id"),
        category_id=data.get("category_id")
    ).first()

    if not link:
        return jsonify({"message": "product category not found"}), 404

    try:
        db.session.delete(link)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete product-category link"}), 400

    return jsonify({"message": "product category deleted"}), 200

