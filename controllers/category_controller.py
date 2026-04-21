
from flask import jsonify, request
from db import db
from models import Categories, category_schema, categories_schema
from util.reflection import populate_object


def add_category():
    data = request.form if request.form else request.get_json()

    new_category = Categories(
        category_name=data.get("category_name"),
        active=data.get("active", True)
    )

    try:
        db.session.add(new_category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create category"}), 400

    return jsonify({
        "message": "category created",
        "result": category_schema.dump(new_category)
    }), 201


def get_all_categories():
    categories = Categories.query.all()
    return jsonify({
        "message": "categories retrieved",
        "results": categories_schema.dump(categories)
    }), 200


def get_category_by_id(category_id):
    category = Categories.query.filter_by(category_id=category_id).first()

    if not category:
        return jsonify({"message": "category not found"}), 404

    return jsonify({
        "message": "category retrieved",
        "result": category_schema.dump(category)
    }), 200


def update_category_by_id(category_id):
    category = Categories.query.filter_by(category_id=category_id).first()

    if not category:
        return jsonify({"message": "category not found"}), 404

    data = request.form if request.form else request.get_json()
    populate_object(category, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update category"}), 400

    return jsonify({
        "message": "category updated",
        "result": category_schema.dump(category)
    }), 200


def delete_category_by_id(category_id):
    category = Categories.query.filter_by(category_id=category_id).first()

    if not category:
        return jsonify({"message": "category not found"}), 404

    try:
        db.session.delete(category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete category"}), 400

    return jsonify({"message": "category deleted"}), 200
