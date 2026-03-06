# import uuid
# from sqlalchemy.dialects.postgresql import UUID
# import marshmallow as ma

# from db import db

# class Companies(db.Model):
#     __tablename__ = "Companies"

#     company_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     company_name = db.Column(db.String(), nullable=False, unique=True)

#     products = db.relationship("Products", foreign_keys="[Products.company_id]", back_populates='company', cascade="all")

#     def __init__(self, company_name):
#         self.company_name = company_name

#     def new_company_obj():
#         return Companies('')


# class CompaniesSchema(ma.Schema):
#     class Meta:
#         fields = ['company_id', 'company_name']


# company_schema = CompaniesSchema()
# Companies_schema = CompaniesSchema(many=True)


import uuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import product

from db import db

class Companies(db.Model):
    __tablename__ = "companies"

    company_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_name = db.Column(db.String(), nullable=False, unique=True)

    products = db.relationship(
        "Products",
        foreign_keys="Products.company_id",
        back_populates="company",
        cascade="all, delete"
    )

    def __init__(self, company_name):
        self.company_name = company_name


class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Companies
        load_instance = True


company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)