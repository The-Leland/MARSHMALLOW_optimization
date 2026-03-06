import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db


class Warranties(db.Model):
    __tablename__ = "warranties"

    warranty_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    warranty_length = db.Column(db.Integer(), nullable=False)
    warranty_description = db.Column(db.String())
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey("products.product_id"), nullable=False)

    product = db.relationship("Products", foreign_keys=[product_id], back_populates="warranty")

    def __init__(self, warranty_length, warranty_description, product_id):
        self.warranty_length = warranty_length
        self.warranty_description = warranty_description
        self.product_id = product_id


# class WarrantiesSchema(ma.Schema):
#     class Meta:
#         fields = ['warranty_id', 'warranty_length', 'warranty_description', 'product']


# warranty_schema = WarrantiesSchema()
# warranties_schema = WarrantiesSchema(many=True)