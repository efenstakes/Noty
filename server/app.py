from flask import Flask, Blueprint
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

## create app instance
app = Flask(__name__, instance_relative_config=True)

## set application configuration
app.config.from_object('config.Config')

## create app serializer
ma = Marshmallow(app)
jwt = JWTManager(app)


# import application blueprint with routing
from routes import api_bp


app.register_blueprint(api_bp, url_prefix='/api')


## set fallback route handler if route is not found
@app.errorhandler(401)
def not_found(e):
    return { 'error': 'Bad route' }, 404
