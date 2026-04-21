


from flask import Blueprint
from controllers import company_controller

companies = Blueprint("companies", __name__)

@companies.route("/company", methods=["POST"])
def route_add_company():
    return company_controller.add_company()

@companies.route("/companies", methods=["GET"])
def route_get_all_companies():
    return company_controller.get_all_companies()

@companies.route("/company/<company_id>", methods=["GET"])
def route_get_company_by_id(company_id):
    return company_controller.get_company_by_id(company_id)

@companies.route("/company/<company_id>", methods=["PUT"])
def route_update_company(company_id):
    return company_controller.update_company_by_id(company_id)

@companies.route("/company/<company_id>", methods=["DELETE"])
def route_delete_company(company_id):
    return company_controller.delete_company_by_id(company_id)
