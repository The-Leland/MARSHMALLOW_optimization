


from flask import Blueprint
from controllers import category_controller

categories = Blueprint("categories", __name__)

@categories.route("/category", methods=["POST"])
def route_add_category():
    return category_controller.add_category()

@categories.route("/categories", methods=["GET"])
def route_get_all_categories():
    return category_controller.get_all_categories()

@categories.route("/category/<category_id>", methods=["GET"])
def route_get_category_by_id(category_id):
    return category_controller.get_category_by_id(category_id)

@categories.route("/category/<category_id>", methods=["PUT"])
def route_update_category(category_id):
    return category_controller.update_category_by_id(category_id)

@categories.route("/category/<category_id>", methods=["DELETE"])
def route_delete_category(category_id):
    return category_controller.delete_category_by_id(category_id)
