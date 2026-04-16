

from models.company import Companies
from util.reflection import populate_object
from db import db


def add_company(data):
    new_company = Companies(
        company_name=data.get("company_name")
    )
    db.session.add(new_company)
    db.session.commit()
    return new_company


def get_all_companies():
    return db.session.query(Companies).all()


def get_company_by_id(company_id):
    return Companies.query.get(company_id)


def update_company_by_id(company_id, data):
    company = db.session.query(Companies).filter_by(company_id=company_id).first()

    if not company:
        return None

    populate_object(company, data)
    db.session.commit()

    return company


def delete_company_by_id(company_id):
    company = Companies.query.get(company_id)

    if company is None:
        return None

    db.session.delete(company)
    db.session.commit()
    return company