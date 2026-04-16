
from db import db
from util.reflection import reflect_table
import marshmallow as ma

class Warranties(db.Model):
    __table__ = reflect_table("warranties")

class WarrantiesSchema(ma.Schema):
    class Meta:
        fields = ["warranty_id", "product_id", "warranty_months"]

warranties_schema = WarrantiesSchema()
warranties_list_schema = WarrantiesSchema(many=True)