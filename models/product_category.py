

from db import db
from sqlalchemy.dialects.postgresql import UUID

class ProductsCategoriesXref(db.Model):
    __tablename__ = "productscategoriesxref"

    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey("products.product_id"), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"), primary_key=True)
