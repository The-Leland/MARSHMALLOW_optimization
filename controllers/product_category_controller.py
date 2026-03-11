from models.product_category import ProductCategory
from models.product import Products
from models.category import Categories
from db import db

from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ProductCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductCategory
        load_instance = True
        include_fk = True

product_category_schema = ProductCategorySchema()
product_categories_schema = ProductCategorySchema(many=True)


def add_product_category(data):
    product_id = data.get("product_id")
    category_id = data.get("category_id")

    new_link = ProductCategory(
        product_id=product_id,
        category_id=category_id
    )

    db.session.add(new_link)
    db.session.commit()

    return new_link


def get_all_product_categories():
    return ProductCategory.query.all()


def get_categories_for_product(product_id):
    links = ProductCategory.query.filter_by(product_id=product_id).all()

    categories = []
    for link in links:
        category = Categories.query.get(link.category_id)
        if category:
            categories.append({
                "category_id": category.category_id,
                "category_name": category.category_name
            })

    return categories


def delete_product_category(data):
    product_id = data.get("product_id")
    category_id = data.get("category_id")

    link = ProductCategory.query.filter_by(
        product_id=product_id,
        category_id=category_id
    ).first()

    if link:
        db.session.delete(link)
        db.session.commit()

    return True