


import marshmallow as ma
from db import db

class Categories(db.Model):
    __tablename__ = "Categories"

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    products = db.relationship(
        "Products",
        secondary="productscategoriesxref",
        back_populates="categories"
    )

    def __init__(self, category_name, active=True):
        self.category_name = category_name
        self.active = active


class CategoriesSchema(ma.Schema):
    class Meta:
        fields = ["category_id", "category_name", "active", "products"]

    category_id = ma.fields.Integer()
    category_name = ma.fields.String()
    active = ma.fields.Boolean()

    products = ma.fields.Nested("ProductsSchema", many=True, exclude=["categories"])


category_schema = CategoriesSchema()
categories_schema = CategoriesSchema(many=True)


