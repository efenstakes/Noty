from flask_restful import Resource, reqparse

## import app models
from models.task import Task
from models.user import User


## add
class TaskAdd(Resource):

    def post(self):
        responze = { 'saved': False, 'id': None }


        return responze

## update
class TaskUpdate(Resource):

    def put(self, id):
        responze = { 'updated': False }

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

    def post(self, id):
        responze = { 'saved': False, 'id': None }

        return responze

    def delete(self, id):
        responze = { 'deleted': False }

        return responze
