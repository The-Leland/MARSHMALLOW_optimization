

from flask import Blueprint
from controllers import product_controller

products = Blueprint("products", __name__)

@products.route("/product", methods=["POST"])
def route_add_product():
    return product_controller.add_product()

@products.route("/products", methods=["GET"])
def route_get_all_products():
    return product_controller.get_all_products()

@products.route("/product/<product_id>", methods=["GET"])
def route_get_product_by_id(product_id):
    return product_controller.get_product_by_id(product_id)

@products.route("/product/<product_id>", methods=["PUT"])
def route_update_product(product_id):
    return product_controller.update_product_by_id(product_id)

@products.route("/product/<product_id>", methods=["DELETE"])
def route_delete_product(product_id):
    return product_controller.delete_product_by_id(product_id)

@products.route("/products/active", methods=["GET"])
def route_get_active_products():
    return product_controller.get_active_products()

@products.route("/product/company/<company_id>", methods=["GET"])
def route_get_products_by_company(company_id):
    return product_controller.get_products_by_company(company_id)
