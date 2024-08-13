from flask import Flask
from flask_pymongo import PyMongo
from app.routes import main
import os
def create_app():
    app = Flask(__name__)
    # Load configuration from .env
    app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost:27017/twitter_db')
    mongo = PyMongo(app)
    # Register blueprints
    app.register_blueprint(main)
    return app