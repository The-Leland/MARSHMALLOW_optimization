



from flask import Flask
import os

from db import db, init_db

from routes.product_routes import products
from routes.company_routes import company
from routes.category_routes import category
from routes.warranty_routes import warranty
from routes.product_category_routes import product_category

flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_PORT")

database_scheme = os.environ.get("DATABASE_SCHEME")
database_user = os.environ.get("DATABASE_USER")
database_password = os.environ.get("DATABASE_PASSWORD")
database_address = os.environ.get("DATABASE_ADDRESS")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"{database_scheme}{database_user}:{database_password}"
    f"@{database_address}:{database_port}/{database_name}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app)

app.register_blueprint(products)
app.register_blueprint(company)
app.register_blueprint(category)
app.register_blueprint(warranty)
app.register_blueprint(product_category)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")

if __name__ == '__main__':
    create_tables()
    app.run(host=flask_host, port=flask_port)
