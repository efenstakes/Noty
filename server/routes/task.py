from flask_restful import Resource, reqparse

from flask_jwt_extended import jwt_required, current_user

## import app models
from models import User, Task


## import app serializer/deserializers
from schemas import user_schema, users_schema, task_schema, tasks_schema


## add
class TaskAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='Task title should be provided')
    parser.add_argument('body', type=str, required=True, help='Task description should be provided')
    parser.add_argument('start_on', type=str, required=False, help='Start date should be provided')
    parser.add_argument('ends_on', type=str, required=False, help='End date should be provided')
    parser.add_argument('participants', type=list, required=True, help='Participants should be provided')

    @jwt_required
    def post(self):
        responze = { 'saved': False, 'task': None }

        # get request data
        data = self.parser.parse_args()

        try:
            task = Task(
                      user=current_user.id, title=data['title'],
                      body=data['body'], start_on=data['start_on'],
                      ends_on=data['ends_on'], 
                      participants=data['participants']
            )
            task.save()
        except:
            return responze, 500

        responze['saved'] = True 
        responze['task'] = task_schema.dump(task)
        return responze

## update
class TaskUpdate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help='Task title should be provided')
    parser.add_argument('body', type=str, required=True, help='Task description should be provided')
    parser.add_argument('start_on', type=str, required=True, help='Start date should be provided')
    parser.add_argument('ends_on', type=str, required=True, help='End date should be provided')
    parser.add_argument('participants', type=list, required=True, help='Participants should be provided')

    @jwt_required
    def put(self, id):
        responze = { 'updated': False }

        # get request data
        data = self.parser.parse_args()

        return responze

## detail
class TaskDetail(Resource):

    @jwt_required
    def get(self, id):
        responze = { 'task': {} }

        try:
            task = Task(id=id, user=current_user.id).get()
        except:
            return responze, 404

        responze['task'] = task
        return responze

## delete
class TaskDelete(Resource):

    @jwt_required
    def delete(self, id):
        responze = { 'deleted': False }

        try:
            task = Task(id=id, user=current_user.id).delete()
        except:
            return responze, 404

        responze['deleted'] = True
        return responze


## mark as complete
class TaskComplete(Resource):

    @jwt_required
    def post(self, id):
        responze = { 'updated': False }

        try:
            task = Task(id=id, user=current_user.id).get()
            task.is_complete = True
            task.save()
        except:
            return responze, 404

        responze['updated'] = True
        return responze


## add or delete participants
class TaskParticipants(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('participants', type=list, required=True, help='Participants should be provided')

    @jwt_required
    def post(self, id):
        responze = { 'saved': False, 'id': None }

        # get request data
        data = self.parser.parse_args()


        return responze

    @jwt_required
    def delete(self, id):
        responze = { 'deleted': False }

        # get request data
        data = self.parser.parse_args()


        return responze
