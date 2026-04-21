

from flask import Blueprint
from controllers import warranty_controller

warranties = Blueprint("warranties", __name__)

@warranties.route("/warranty", methods=["POST"])
def route_add_warranty():
    return warranty_controller.add_warranty()

@warranties.route("/warranties", methods=["GET"])
def route_get_all_warranties():
    return warranty_controller.get_all_warranties()

@warranties.route("/warranty/<warranty_id>", methods=["GET"])
def route_get_warranty_by_id(warranty_id):
    return warranty_controller.get_warranty_by_id(warranty_id)

@warranties.route("/warranty/<warranty_id>", methods=["PUT"])
def route_update_warranty(warranty_id):
    return warranty_controller.update_warranty_by_id(warranty_id)

@warranties.route("/warranty/<warranty_id>", methods=["DELETE"])
def route_delete_warranty(warranty_id):
    return warranty_controller.delete_warranty_by_id(warranty_id)
