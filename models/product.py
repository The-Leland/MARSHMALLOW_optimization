
from db import db
from util.reflection import reflect_table
import marshmallow as ma

from models.company import CompaniesSchema
from models.category import CategoriesSchema
from models.warranty import WarrantiesSchema

class Products(db.Model):
    __table__ = reflect_table("products")

    # Relationships preserved exactly as your original design
    company = db.relationship(
        "Companies",
        foreign_keys=[__table__.c.company_id],
        backref="products"
    )

    categories = db.relationship(
        "Categories",
        secondary="products_categories_association",
        backref="products"
    )

    warranty = db.relationship(
        "Warranties",
        foreign_keys="Warranties.product_id",
        uselist=False,
        backref="product"
    )

class ProductsSchema(ma.Schema):
    class Meta:
        fields = [
            "product_id",
            "product_name",
            "description",
            "price",
            "active",
            "company",
            "categories",
            "warranty"
        ]

    company = ma.fields.Nested(CompaniesSchema)
    categories = ma.fields.Nested(CategoriesSchema, many=True)
    warranty = ma.fields.Nested(WarrantiesSchema)

products_schema = ProductsSchema()
products_list_schema = ProductsSchema(many=True)