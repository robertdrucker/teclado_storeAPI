from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

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

# Connects the flask smorest extension to the Flask app.
api = Api(app)

# register blueprints
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)