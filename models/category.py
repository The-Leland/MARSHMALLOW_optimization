


from db import db, ma

class Categories(db.Model):
    __tablename__ = "categories"

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    products = db.relationship(
        "Products",
        secondary="productscategoriesxref",
        back_populates="categories"
    )


class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Categories
        load_instance = True

    category_id = ma.auto_field()
    category_name = ma.auto_field()
    active = ma.auto_field()


