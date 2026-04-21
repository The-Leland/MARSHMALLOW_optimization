


import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Companies(db.Model):
    __tablename__ = "Companies"

    company_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)

    products = db.relationship(
        "Products",
        back_populates="company",
        cascade="all, delete"
    )

    def __init__(self, company_name, description=None, active=True):
        self.company_name = company_name
        self.description = description
        self.active = active


class CompaniesSchema(ma.Schema):
    class Meta:
        fields = ["company_id", "company_name", "description", "active", "products"]

    company_id = ma.fields.UUID()
    company_name = ma.fields.String()
    description = ma.fields.String()
    active = ma.fields.Boolean()

    products = ma.fields.Nested("ProductsSchema", many=True, exclude=["company"])



company_schema = CompaniesSchema()
companies_schema = CompaniesSchema(many=True)
