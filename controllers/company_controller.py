

from flask import jsonify, request
from db import db
from models import Companies, company_schema, companies_schema
from util.reflection import populate_object


def add_company():
    data = request.form if request.form else request.get_json()

    new_company = Companies(
        company_name=data.get("company_name"),
        description=data.get("description"),
        active=data.get("active", True)
    )

    try:
        db.session.add(new_company)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create company"}), 400

    return jsonify({
        "message": "company created",
        "result": company_schema.dump(new_company)
    }), 201


def get_all_companies():
    companies = Companies.query.all()
    return jsonify({
        "message": "companies retrieved",
        "results": companies_schema.dump(companies)
    }), 200


def get_company_by_id(company_id):
    company = Companies.query.filter_by(company_id=company_id).first()

    if not company:
        return jsonify({"message": "company not found"}), 404

    return jsonify({
        "message": "company retrieved",
        "result": company_schema.dump(company)
    }), 200


def update_company_by_id(company_id):
    company = Companies.query.filter_by(company_id=company_id).first()

    if not company:
        return jsonify({"message": "company not found"}), 404

    data = request.form if request.form else request.get_json()
    populate_object(company, data)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update company"}), 400

    return jsonify({
        "message": "company updated",
        "result": company_schema.dump(company)
    }), 200


def delete_company_by_id(company_id):
    company = Companies.query.filter_by(company_id=company_id).first()

    if not company:
        return jsonify({"message": "company not found"}), 404

    try:
        db.session.delete(company)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete company"}), 400

    return jsonify({"message": "company deleted"}), 200

