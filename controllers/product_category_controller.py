from models import ProductsCategoriesXref
from models import Products
from models import Categories
from db import db


def add_product_category(data):
    product_id = data.get("product_id")
    category_id = data.get("category_id")

    new_link = ProductsCategoriesXref(
        product_id=product_id,
        category_id=category_id
    )

    db.session.add(new_link)
    db.session.commit()

    return new_link


def get_all_product_categories():
    return db.session.query(ProductsCategoriesXref).all()


def get_categories_for_product(product_id):
    links = db.session.query(ProductsCategoriesXref).filter_by(product_id=product_id).all()

    categories = []
    for link in links:
        category = db.session.query(Categories).filter_by(category_id=link.category_id).first()
        if category:
            categories.append({
                "category_id": category.category_id,
                "category_name": category.category_name
            })

    return categories


def delete_product_category(data):
    product_id = data.get("product_id")
    category_id = data.get("category_id")

    link = db.session.query(ProductsCategoriesXref).filter_by(
        product_id=product_id,
        category_id=category_id
    ).first()

    if not link:
        return None

    db.session.delete(link)
    db.session.commit()

    return link

