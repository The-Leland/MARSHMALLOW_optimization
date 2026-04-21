


from flask import Blueprint, request, jsonify

from controllers.company_controller import (
    add_company,
    get_all_companies,
    get_company_by_id,
    update_company_by_id,
    delete_company_by_id
)

from models.company import CompanySchema

company = Blueprint('company', __name__)


@company.route('/company', methods=['POST'])
def add_company_route():
    data = request.get_json()
    new_company = add_company(data)
    return jsonify({
        "message": "company created",
        "result": CompanySchema().dump(new_company)
    }), 201


@company.route('/companies', methods=['GET'])
def get_all_companies_route():
    companies = get_all_companies()
    return jsonify({
        "message": "companies retrieved",
        "results": CompanySchema(many=True).dump(companies)
    }), 200


@company.route('/company/<company_id>', methods=['GET'])
def get_company_route(company_id):
    company_obj = get_company_by_id(company_id)

    if company_obj is None:
        return jsonify({"message": "company not found"}), 404

    return jsonify({
        "message": "company retrieved",
        "result": CompanySchema().dump(company_obj)
    }), 200


@company.route('/company/<company_id>', methods=['PUT'])
def update_company_route(company_id):
    data = request.get_json()
    updated_company = update_company_by_id(company_id, data)

    if updated_company is None:
        return jsonify({"message": "company not found"}), 404

    return jsonify({
        "message": "company updated",
        "result": CompanySchema().dump(updated_company)
    }), 200


@company.route('/company/<company_id>', methods=['DELETE'])
def delete_company_route(company_id):
    deleted = delete_company_by_id(company_id)

    if deleted is None:
        return jsonify({"message": "company not found"}), 404

    return jsonify({"message": "company deleted"}), 200
