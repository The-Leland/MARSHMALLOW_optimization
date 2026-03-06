# from flask import Blueprint, 

# import controllers


# company=Blueprint('company', __name__)

# @company.route('/company', methods=["POST"])
# def add_company():
#     return controllers.add_company()


# @company.route("/company/<company_id>", method=["PUT"])
# def update_company_by_id(company_id):
#     return controllers.updata_company_by_id(company_id)



from flask import Blueprint, request, jsonify

from controllers.company_controller import (
    add_company,
    get_all_companies,
    update_company_by_id
)
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