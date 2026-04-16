

from db import db
from util.reflection import reflect_table
import marshmallow as ma

class Companies(db.Model):
    __table__ = reflect_table("companies")

class CompaniesSchema(ma.Schema):
    class Meta:
        fields = ["company_id", "company_name"]

companies_schema = CompaniesSchema()
companies_list_schema = CompaniesSchema(many=True)