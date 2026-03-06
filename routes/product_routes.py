

from flask import Blueprint
import controllers
from controllers.product_controller import product_schema, products_schema

products = Blueprint('products', __name__)


@products.route('/product', methods=['POST'])
def add_product_route():
    return controllers.add_product()


@products.route('/products', methods=['GET'])
def get_all_products_route():
    return controllers.get_all_products()


@products.route('/product/<product_id>', methods=['GET'])
def get_product_by_id_route(product_id):
    return controllers.get_product_by_id(product_id)


@products.route('/product/<product_id>', methods=['PUT'])
def update_product_route(product_id):
    return controllers.update_product_by_id(product_id)


@products.route('/product/<product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    return controllers.delete_product_by_id(product_id)