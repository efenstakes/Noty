from flask import Blueprint

## create application base routing blueprint
api_bp = Blueprint('app_api', __name__)

## import app resources and hook them to the blueprint


## test route
@api_bp.route('/')
def test():
    return 'app works'