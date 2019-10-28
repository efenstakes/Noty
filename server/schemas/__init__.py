
from .task import TaskSchema
from .user import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

