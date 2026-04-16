

from flask import Blueprint, request, jsonify

from controllers.product_controller import (
    add_product,
    get_all_products,
    get_product_by_id,
    update_product_by_id,
    delete_product_by_id
)

from models.product import products_schema, products_list_schema

products = Blueprint('products', __name__)


@products.route('/product', methods=['POST'])
def add_product_route():
    data = request.get_json()
    new_product = add_product(data)
    return jsonify({
        "message": "product created",
        "result": products_schema.dump(new_product)
    }), 201


@products.route('/products', methods=['GET'])
def get_all_products_route():
    all_products = get_all_products()
    return jsonify({
        "message": "products retrieved",
        "results": products_list_schema.dump(all_products)
    }), 200


@products.route('/product/<product_id>', methods=['GET'])
def get_product_by_id_route(product_id):
    product_obj = get_product_by_id(product_id)

    if product_obj is None:
        return jsonify({"message": "product not found"}), 404

    return jsonify({
        "message": "product retrieved",
        "result": products_schema.dump(product_obj)
    }), 200


@products.route('/product/<product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.get_json()
    updated_product = update_product_by_id(product_id, data)

    if updated_product is None:
        return jsonify({"message": "product not found"}), 404

    return jsonify({
        "message": "product updated",
        "result": products_schema.dump(updated_product)
    }), 200


@products.route('/product/<product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    deleted = delete_product_by_id(product_id)

    if deleted is None:
        return jsonify({"message": "product not found"}), 404

    return jsonify({"message": "product deleted"}), 200