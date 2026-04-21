


import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma

class Companies(db.Model):
    __tablename__ = "companies"

    company_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=True)

    products = db.relationship(
        "Products",
        back_populates="company",
        cascade="all, delete"
    )


class CompanySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Companies
        load_instance = True
        include_relationships = True

    company_id = ma.auto_field()
    company_name = ma.auto_field()

