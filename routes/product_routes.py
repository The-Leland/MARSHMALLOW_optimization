

from flask import Blueprint, request, jsonify

from controllers.product_controller import (
    add_product,
    get_all_products,
    get_product_by_id,
    update_product_by_id,
    delete_product_by_id,
    get_active_products,
    get_products_by_company
)

from models.product import ProductSchema

products = Blueprint('products', __name__)


@products.route('/product', methods=['POST'])
def add_product_route():
    data = request.get_json()
    new_product = add_product(data)
    return jsonify({
        "message": "product created",
        "result": ProductSchema().dump(new_product)
    }), 201


@products.route('/products', methods=['GET'])
def get_all_products_route():
    all_products = get_all_products()
    return jsonify({
        "message": "products retrieved",
        "results": ProductSchema(many=True).dump(all_products)
    }), 200


@products.route('/product/<product_id>', methods=['GET'])
def get_product_by_id_route(product_id):
    product_obj = get_product_by_id(product_id)

    if product_obj is None:
        return jsonify({"message": "product not found"}), 404

    return jsonify({
        "message": "product retrieved",
        "result": ProductSchema().dump(product_obj)
    }), 200


@products.route('/product/<product_id>', methods=['PUT'])
def update_product_route(product_id):
    data = request.get_json()
    updated_product = update_product_by_id(product_id, data)

    if updated_product is None:
        return jsonify({"message": "product not found"}), 404

    return jsonify({
        "message": "product updated",
        "result": ProductSchema().dump(updated_product)
    }), 200


@products.route('/product/<product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    deleted = delete_product_by_id(product_id)

    if deleted is None:
        return jsonify({"message": "product not found"}), 404

    return jsonify({"message": "product deleted"}), 200


@products.route('/products/active', methods=['GET'])
def get_active_products_route():
    active_products = get_active_products()
    return jsonify({
        "message": "active products retrieved",
        "results": ProductSchema(many=True).dump(active_products)
    }), 200


@products.route('/product/company/<company_id>', methods=['GET'])
def get_products_by_company_route(company_id):
    company_products = get_products_by_company(company_id)
    return jsonify({
        "message": "products retrieved for company",
        "results": ProductSchema(many=True).dump(company_products)
    }), 200
