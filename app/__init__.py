from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://mongo:27017/ecommerce"

    client = MongoClient(app.config["MONGO_URI"])
    app.db = client.get_database()

    from .routes import main
    app.register_blueprint(main)

    return app
