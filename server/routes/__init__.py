from flask import Blueprint
from flask_restful import Api

# from app import app

## create application base routing blueprint
api_bp = Blueprint('app_api', __name__)
api = Api(api_bp)

## import app resources and hook them to the blueprint
from .user import (
    UserAdd, UserDetails, UserUpdate, UserDelete, UserLogin, 
    UserLogout, UserTasks
)
from .task import (
    TaskAdd, TaskUpdate, TaskComplete, TaskDelete, TaskDetail, 
    TaskAll, TaskParticipants
)


## create user routes
api.add_resource(UserAdd, '/account')
api.add_resource(UserDetails, '/account/<id>')
api.add_resource(UserUpdate, '/account/<id>')
api.add_resource(UserDelete, '/account/<id>')
api.add_resource(UserTasks, '/account/<id>/tasks')
api.add_resource(UserLogin, '/account/login')
api.add_resource(UserLogout, '/account/logout')

## create task routes
api.add_resource(TaskAdd, '/task')
api.add_resource(TaskDetail, '/task/<id>')
api.add_resource(TaskUpdate, '/task/<id>')
api.add_resource(TaskComplete, '/task/<id>/complete')
api.add_resource(TaskDelete, '/task/<id>')
api.add_resource(TaskAll, '/task/<id>')
api.add_resource(TaskParticipants, '/task/<id>/participants')


## test route
@api_bp.route('/')
def test():
    return 'app works'