

from db import db
from util.reflection import reflect_table

class ProductCategory(db.Model):
    __table__ = reflect_table("products_categories_association")