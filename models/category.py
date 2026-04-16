


from db import db
from util.reflection import reflect_table
import marshmallow as ma

class Categories(db.Model):
    __table__ = reflect_table("categories")

class CategoriesSchema(ma.Schema):
    class Meta:
        fields = ["category_id", "category_name"]

categories_schema = CategoriesSchema()
categories_list_schema = CategoriesSchema(many=True)