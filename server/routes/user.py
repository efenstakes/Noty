from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash
import mongoengine
import datetime
from flask_jwt_extended import (
    jwt_required, current_user, create_access_token
)

## import app models
from models import User, Task

## import app serializer/deserializers
from schemas import user_schema, users_schema, task_schema, tasks_schema


## add user
class UserAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name should be provided')
    parser.add_argument('email', type=str, required=True, help='Email should be provided')
    parser.add_argument('password', type=str, required=True, help='Password should be provided')
    parser.add_argument('password_confirmation', type=str, required=True, help='Password confirmation should be provided')

    def post(self):
        responze = { 'saved': False, 'user': None, 'errors': [] }
        # get request data
        data = self.parser.parse_args()
        
        try:
            user = User( 
                    name=data['name'], email=data['email'], 
                    password=generate_password_hash(data['password']) 
                )
            user.save()
        except:
            return responze, 500
        
        responze['saved'] = True 
        responze['user'] = user_schema.dump(user)
        return responze


## get user details
class UserDetails(Resource):
    
    @jwt_required
    def get(self, id):
        responze = { 'user': {} }

        try:
            user = User.objects(id=id).get()
        except ( mongoengine.errors.ValidationError, mongoengine.errors.DoesNotExist ):
            return responze, 404

        responze['user'] = user_schema.dump(user)
        return responze


## update user details
class UserUpdate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name should be provided')
    parser.add_argument('email', type=str, required=True, help='Email should be provided')

    @jwt_required
    def post(self, id):
        responze = { 'updated': False, 'user': {} }
        
        # get request data
        data = self.parser.parse_args()

        try:
            user = User.objects(id=id).get()
            user.email = data['email']
            user.name = data['name']
            
            user.save()
        except:
            return responze, 404

        responze['updated'] = True
        responze['user'] = user_schema.dump(user)
        return responze


## delete user 
class UserDelete(Resource):
    
    @jwt_required
    def delete(self, id):
        responze = { 'deleted': False }

        try:
            user = User.objects(id=id).delete()
        except ( mongoengine.errors.ValidationError, mongoengine.errors.DoesNotExist ):
            return responze, 404

        responze['deleted'] = True
        return responze, 200


## login user
class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='Email should be provided')
    parser.add_argument('password', type=str, required=True, help='Password should be provided')

    def post(self):
        responze = { 'user': {}, 'token': None }

        # get request data
        data = self.parser.parse_args()
        
        try:
            user = User.objects( email=data['email'] ).get()
            print('user found {}'.format(user.email))
            if not user.is_hash_match(data['password']):
                raise 'Bad Password'
        except:
            return responze, 404

        responze['user'] = user_schema.dump(user)
        responze['token'] = create_access_token(
                                str(user.id),
                                expires_delta=datetime.timedelta(minutes=59)
                            )
        return responze


## logout user
class UserLogout(Resource):
    
    @jwt_required
    def post(self):
        responze = { 'logged_out': False }

        return responze


class UserTasks(Resource):

    @jwt_required
    def get(self, id):
        responze = { 'tasks': [] }

        try:
            tasks = Task.objects(user=id)
        except:
            return responze, 500

        responze['tasks'] = tasks_schema.dump(tasks)
        return responze
    