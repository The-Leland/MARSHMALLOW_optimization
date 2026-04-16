from flask import Blueprint, request, jsonify

from controllers.product_category_controller import (
    add_product_category,
    get_all_product_categories,
    get_categories_for_product,
    delete_product_category
)

from models.product_category import product_category_schema, product_categories_schema

product_category = Blueprint('product_category', __name__)


@product_category.route('/product-category', methods=['POST'])
def add_product_category_route():
    data = request.get_json()
    new_link = add_product_category(data)
    return jsonify({
        "message": "product category created",
        "result": product_category_schema.dump(new_link)
    }), 201


@product_category.route('/product-categories', methods=['GET'])
def get_all_product_categories_route():
    links = get_all_product_categories()
    return jsonify({
        "message": "product categories retrieved",
        "results": product_categories_schema.dump(links)
    }), 200


@product_category.route('/product-category/get', methods=['POST'])
def get_categories_for_product_route():
    data = request.get_json()
    product_id = data.get("product_id")
    categories = get_categories_for_product(product_id)
    return jsonify({
        "message": "categories retrieved for product",
        "results": categories
    }), 200


@product_category.route('/product-category', methods=['DELETE'])
def delete_product_category_route():
    data = request.get_json()
    deleted = delete_product_category(data)

    if deleted is None:
        return jsonify({"message": "product category not found"}), 404

    return jsonify({"message": "product category deleted"}), 200
