

import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from db import db


class ProductsCategoriesXref(db.Model):
    __tablename__ = "ProductsCategoriesXref"

    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Products.product_id"), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("Categories.category_id"), primary_key=True)

    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id


class ProductsCategoriesXrefSchema(ma.Schema):
    class Meta:
        fields = ["product_id", "category_id"]

    product_id = ma.fields.UUID()
    category_id = ma.fields.Integer()


product_category_schema = ProductsCategoriesXrefSchema()
product_categories_schema = ProductsCategoriesXrefSchema(many=True)
