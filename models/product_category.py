from db import db
from sqlalchemy.dialects.postgresql import UUID



class ProductCategory(db.Model):
    __tablename__ = "products_categories_association"

    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey("products.product_id"), primary_key=True)
    category_id = db.Column(UUID(as_uuid=True), db.ForeignKey("categories.category_id"), primary_key=True)

    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id

