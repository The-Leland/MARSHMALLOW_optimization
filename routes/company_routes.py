


from flask import Blueprint, request, jsonify

from controllers.company_controller import (
    add_company,
    get_all_companies,
    get_company_by_id,
    update_company_by_id,
    delete_company_by_id
)

from db import db

from controllers.company_controller import company_schema, companies_schema
from models.company import Companies

company = Blueprint('company', __name__)


@company.route('/company', methods=['POST'])
def add_company_route():
    data = request.get_json()
    new_company = add_company(data)
    return jsonify({
        "message": "company created",
        "result": company_schema.dump(new_company)
    }), 201


@company.route('/companies', methods=['GET'])
def get_all_companies_route():
    companies = get_all_companies()
    return jsonify({
        "message": "companies retrieved",
        "results": companies_schema.dump(companies)
    }), 200


@company.route('/company/<company_id>', methods=['GET'])
def get_company_route(company_id):
    company = get_company_by_id(company_id)

    if company is None:
        return jsonify({"message": "company not found"}), 404

    return jsonify({
        "message": "company retrieved",
        "result": company_schema.dump(company)
    }), 200


@company.route('/company/<company_id>', methods=['PUT'])
def update_company_route(company_id):
    data = request.get_json()
    updated_company = update_company_by_id(company_id, data)

    if updated_company is None:
        return jsonify({"message": "company not found"}), 404

    return jsonify({
        "message": "company updated",
        "result": company_schema.dump(updated_company)
    }), 200


@company.route('/company/<company_id>', methods=['DELETE'])
def delete_company_route(company_id):
    company = Companies.query.get(company_id)

    if company is None:
        return jsonify({"message": "company not found"}), 404

    db.session.delete(company)
    db.session.commit()

    return jsonify({"message": "company deleted"}), 200