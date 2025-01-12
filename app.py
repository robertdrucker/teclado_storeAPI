import os

from flask import Flask
from flask_smorest import Api

from db import db

# same as import __
# import models.__init__
# We need to import our models before we use the SQLAlchemy extension
import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBluePrint

# App factory function (factory pattern)
# Creates an app instance and application context
# create_app is automatically called by Flask
def create_app(db_url=None):
    app = Flask(__name__)
    # This is a Flask configuration that handles propogation of 
    # exceptions hidden within Flask extension(s) so that they are 
    # or are not propogated into the main app so we can see it.
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # Flask smorest configuation
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"

    # OPENAPI is a standard for API documentation.
    # This tells Flask smorest to use 3.0.3.
    app.config["OPENAPI_VERSION"] = "3.0.3"

    # Tells Flask smorest where the root of the API is.
    app.config["OPENAPI_URL_PREFIX"] = "/"

    # Documentation configurations for swagger-ui path

    # This tells Flask smorest to use swagger-ur for the 
    # documentation that is in /swagger-ui.
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"

    # cdn for swagger documentation code
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    # Define and add flask_sqlalchemy to the Flask app
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")

    # Disable Flask-SQLAlchemy's event notification system that otherwise would 
    #  get layered on top of SQLAlchemy.
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the Flask-SQLAlchemy extension and pass it the Flask app
    #  so that it can connect to the app.
    db.init_app(app)

    # Connects the flask smorest extension to the Flask app.
    api = Api(app)

    # creates an application context. This context is essential for accessing 
    # application-level data and functionality within a specific block of code.
    # It pushes the application context onto the stack, making it the active context.
    with app.app_context():
        # If not present, create all tables in our database
        db.create_all() 

    # register blueprints
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBluePrint)

    return app 