from flask import Blueprint
from controllers import product_category_controller

product_category = Blueprint("product_category", __name__)

@product_category.route("/product-category", methods=["POST"])
def route_add_product_category():
    return product_category_controller.add_product_category()

@product_category.route("/product-categories", methods=["GET"])
def route_get_all_product_categories():
    return product_category_controller.get_all_product_categories()

@product_category.route("/product-category/get", methods=["POST"])
def route_get_categories_for_product():
    return product_category_controller.get_categories_for_product(
        request.get_json().get("product_id")
    )

@product_category.route("/product-category", methods=["DELETE"])
def route_delete_product_category():
    return product_category_controller.delete_product_category()
