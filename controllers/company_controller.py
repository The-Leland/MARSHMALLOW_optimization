# from flask import jsonify

# from models.company import Companies, company_schema, Companies_schema
# from util.reflection import populate_object
# from db import db

# def add_company(request):
#     post_data = request.form if request.form else request.json

#     new_company = Companies.new_company_obj()
#     populate_object(new_company, post_data)

#     db.session.add(new_company)
#     db.session.commit()

#     return jsonify({"message": "company created", "result": company_schema.dump(new_company)}), 201

# def get_all_companies():
#     companies_query = db.session.query(Companies).all()

#     return jsonify({"message": "companies retrieved"})


# def updata_company_by_id(company_id):
#     post_data = request.form if request.form else request.json
#     company_query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

#     if not company_query:
#         return jsonify({"message": "company not found"}), 404
    
#     populate_object(company_query, post_data)
#     db.session.commit()

#     return jsonify({"message": "company updated", "result": company_schema.dump(company_query)}), 200



from models.company import Companies
from util.reflection import populate_object
from db import db

from marshmallow import Schema, fields

class CompanySchema(Schema):
    company_id = fields.UUID()
    company_name = fields.String()
    # add other fields your model uses

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)

def add_company(data):
    new_company = Companies(company_name="")
    populate_object(new_company, data)

    db.session.add(new_company)
    db.session.commit()

    return new_company


def get_all_companies():
    return db.session.query(Companies).all()


def update_company_by_id(company_id, data):
    company = db.session.query(Companies).filter_by(company_id=company_id).first()

    if not company:
        return None

    populate_object(company, data)
    db.session.commit()

    return company

