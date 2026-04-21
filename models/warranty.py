

import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma


class Warranties(db.Model):
    __tablename__ = "warranties"

    warranty_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey("products.product_id"), nullable=False)
    warranty_months = db.Column(db.Integer, nullable=False)

    product = db.relationship(
        "Products",
        back_populates="warranty"
    )


class WarrantySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Warranties
        load_instance = True
        include_relationships = True

    warranty_id = ma.auto_field()
    product_id = ma.auto_field()
    warranty_months = ma.auto_field()

