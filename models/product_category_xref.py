import uuid
from sqlalchemy.dialects.postgresql import UUID
# import marshmallow as ma

from db import db


product_category_association_table = db.Table(
    "products_categories_association",
    db.Column("product_id", UUID(as_uuid=True), db.ForeignKey("products.product_id"), primary_key=True),
    db.Column("category_id", UUID(as_uuid=True), db.ForeignKey("categories.category_id"), primary_key=True)
)


# class ProductCategoryXrefSchema(ma.Schema):
#     class Meta:
#         fields = ["product_id", "category_id"]


# product_category_xref_schema = ProductCategoryXrefSchema()
# product_category_xrefs_schema = ProductCategoryXrefSchema(many=True)

