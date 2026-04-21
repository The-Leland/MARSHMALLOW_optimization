
import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db, ma

class Products(db.Model):
    __tablename__ = "products"

    product_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_id = db.Column(UUID(as_uuid=True), db.ForeignKey("companies.company_id"), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2))
    active = db.Column(db.Boolean, default=True)

    company = db.relationship("Companies", back_populates="products")
    categories = db.relationship("Categories", secondary="productscategoriesxref", back_populates="products")
    warranty = db.relationship("Warranties", back_populates="product", uselist=False, cascade="all, delete")

class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Products
        load_instance = True
        include_relationships = True

    product_id = ma.auto_field()
    company_id = ma.auto_field()
    description = ma.auto_field()
    price = ma.auto_field()
    active = ma.auto_field()

    company = ma.Nested("CompanySchema", exclude=["products"])
    categories = ma.Nested("CategorySchema", many=True, exclude=["products"])
    warranty = ma.Nested("WarrantySchema", exclude=["product"])

