

from flask import Blueprint, request, jsonify

from controllers.warranty_controller import (
    add_warranty,
    get_all_warranties,
    get_warranty_by_id,
    update_warranty_by_id,
    delete_warranty_by_id
)

from models.warranty import WarrantySchema

warranty = Blueprint('warranty', __name__)


@warranty.route('/warranty', methods=['POST'])
def add_warranty_route():
    data = request.get_json()
    new_warranty = add_warranty(data)
    return jsonify({
        "message": "warranty created",
        "result": WarrantySchema().dump(new_warranty)
    }), 201


@warranty.route('/warranties', methods=['GET'])
def get_all_warranties_route():
    all_warranties = get_all_warranties()
    return jsonify({
        "message": "warranties retrieved",
        "results": WarrantySchema(many=True).dump(all_warranties)
    }), 200


@warranty.route('/warranty/<warranty_id>', methods=['GET'])
def get_warranty_by_id_route(warranty_id):
    warranty_obj = get_warranty_by_id(warranty_id)

    if warranty_obj is None:
        return jsonify({"message": "warranty not found"}), 404

    return jsonify({
        "message": "warranty retrieved",
        "result": WarrantySchema().dump(warranty_obj)
    }), 200


@warranty.route('/warranty/<warranty_id>', methods=['PUT'])
def update_warranty_by_id_route(warranty_id):
    data = request.get_json()
    updated_warranty = update_warranty_by_id(warranty_id, data)

    if updated_warranty is None:
        return jsonify({"message": "warranty not found"}), 404

    return jsonify({
        "message": "warranty updated",
        "result": WarrantySchema().dump(updated_warranty)
    }), 200


@warranty.route('/warranty/<warranty_id>', methods=['DELETE'])
def delete_warranty_route(warranty_id):
    deleted = delete_warranty_by_id(warranty_id)

    if deleted is None:
        return jsonify({"message": "warranty not found"}), 404

    return jsonify({"message": "warranty deleted"}), 200
