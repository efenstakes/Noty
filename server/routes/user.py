from flask_restful import Resource, reqparse

## import app models
from models.task import Task
from models.user import User


## add user
class UserAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name should be provided')
    parser.add_argument('email', type=str, required=True, help='Email should be provided')
    parser.add_argument('password', type=str, required=True, help='Password should be provided')
    parser.add_argument('password_confirmation', type=str, required=True, help='Password confirmation should be provided')

    def post(self):
        responze = { 'saved': False, 'id': None }
        # get request data
        data = self.parser.parse_args()

        print(data['name'])

        return responze


## get user details
class UserDetails(Resource):
    
    def get(self, id):
        responze = { 'user': {} }

        return responze

## update user details
class UserUpdate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name should be provided')
    parser.add_argument('email', type=str, required=True, help='Email should be provided')

    def post(self, id):
        responze = { 'updated': False }
        
        # get request data
        data = self.parser.parse_args()

        return responze

## delete user 
class UserDelete(Resource):
    
    def delete(self, id):
        responze = { 'deleted': False }

        return responze

## login user
class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='Email should be provided')
    parser.add_argument('password', type=str, required=True, help='Password should be provided')

    def post(self):
        responze = { 'user': {}, 'token': None }

        # get request data
        data = self.parser.parse_args()

        return responze

## logout user
class UserLogout(Resource):
    
    def post(self):
        responze = { 'logged_out': False }

        return responze