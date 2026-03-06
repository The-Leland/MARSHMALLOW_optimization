from flask import Blueprint, request, jsonify

from controllers.category_controller import (
    add_category,
    get_all_categories,
    get_category_by_id,
    update_category_by_id,
    delete_category_by_id
)
from controllers.category_controller import category_schema, categories_schema

# from models.category import category_schema, categories_schema

category = Blueprint('category', __name__)


@category.route('/category', methods=['POST'])
def add_category_route():
    data = request.get_json()
    new_category = add_category(data)
    return jsonify({
        "message": "category created",
        "result": category_schema.dump(new_category)
    }), 201


@category.route('/categories', methods=['GET'])
def get_all_categories_route():
    categories = get_all_categories()
    return jsonify({
        "message": "categories retrieved",
        "results": categories_schema.dump(categories)
    }), 200


@category.route('/category/<category_id>', methods=['GET'])
def get_category_by_id_route(category_id):
    category_obj = get_category_by_id(category_id)

    if category_obj is None:
        return jsonify({"message": "category not found"}), 404

    return jsonify({
        "message": "category retrieved",
        "result": category_schema.dump(category_obj)
    }), 200


@category.route('/category/<category_id>', methods=['PUT'])
def update_category_route(category_id):
    data = request.get_json()
    updated_category = update_category_by_id(category_id, data)

    if updated_category is None:
        return jsonify({"message": "category not found"}), 404

    return jsonify({
        "message": "category updated",
        "result": category_schema.dump(updated_category)
    }), 200


@category.route('/category/<category_id>', methods=['DELETE'])
def delete_category_route(category_id):
    deleted = delete_category_by_id(category_id)

    if deleted is None:
        return jsonify({"message": "category not found"}), 404

    return jsonify({"message": "category deleted"}), 200