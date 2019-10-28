from flask_restful import Resource, reqparse

## import app models
from models import User, Task


## import app serializer/deserializers
from schemas import user_schema, users_schema, task_schema, tasks_schema


## add
class TaskAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='Task title should be provided')
    parser.add_argument('body', type=str, required=True, help='Task description should be provided')
    parser.add_argument('start_on', type=str, required=True, help='Start date should be provided')
    parser.add_argument('ends_on', type=str, required=True, help='End date should be provided')
    parser.add_argument('participants', type=list, required=True, help='Participants should be provided')

    def post(self):
        responze = { 'saved': False, 'id': None }

        # get request data
        data = self.parser.parse_args()

        return responze

## update
class TaskUpdate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='Task title should be provided')
    parser.add_argument('body', type=str, required=True, help='Task description should be provided')
    parser.add_argument('start_on', type=str, required=True, help='Start date should be provided')
    parser.add_argument('ends_on', type=str, required=True, help='End date should be provided')
    parser.add_argument('participants', type=list, required=True, help='Participants should be provided')

    def put(self, id):
        responze = { 'updated': False }

        # get request data
        data = self.parser.parse_args()

        return responze

## detail
class TaskDetail(Resource):

    def get(self, id):
        responze = { 'task': {} }

        return responze

## delete
class TaskDelete(Resource):

    def delete(self, id):
        responze = { 'deleted': False }

        return responze


## get all
class TaskAll(Resource):

    def get(self, id):
        responze = { 'tasks': [] }

        return responze


## mark as complete
class TaskComplete(Resource):

    def post(self, id):
        responze = { 'updated': False }

        return responze


## add or delete participants
class TaskParticipants(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('participants', type=list, required=True, help='Participants should be provided')

    def post(self, id):
        responze = { 'saved': False, 'id': None }

        # get request data
        data = self.parser.parse_args()


        return responze

    def delete(self, id):
        responze = { 'deleted': False }

        # get request data
        data = self.parser.parse_args()


        return responze
