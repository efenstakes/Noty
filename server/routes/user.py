from flask_restful import Resource, reqparse

## import app models
from models.task import Task
from models.user import User


## add user
class UserAdd(Resource):

    def post(self):
        responze = { 'saved': False, 'id': None }
        # get request data
        

        return responze


## get user details
class UserDetails(Resource):
    
    def get(self, id):
        responze = { 'user': {} }

        return responze

## update user details
class UserUpdate(Resource):
    
    def post(self, id):
        responze = { 'updated': False }

        return responze

## delete user 
class UserDelete(Resource):
    
    def delete(self, id):
        responze = { 'deleted': False }

        return responze

## login user
class UserLogin(Resource):
    
    def post(self):
        responze = { 'user': {}, 'token': None }

        return responze

## logout user
class UserLogout(Resource):
    
    def post(self):
        responze = { 'logged_out': False }

        return responze