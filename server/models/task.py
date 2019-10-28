import mongoengine
import datetime


class Task(mongoengine.Document):
    title = mongoengine.StringField( max_length=100 )
    body = mongoengine.StringField()
    starts_on = mongoengine.DateTimeField( default=None )
    ends_on = mongoengine.DateTimeField( default=None )
    is_complete = mongoengine.BooleanField( default=False )
    participants = mongoengine.ListField( mongoengine.EmailField() )
    # user = mongoengine.ReferenceField('User', reverse_delete_rule=mongoengine.CASCADE)
    added_on = mongoengine.DateTimeField( default = datetime.datetime.utcnow )

    ## define document name
    meta = { 'collection': 'tasks' }

    def __repr__(self):
        return 'Task >> {0} starts on >> {1} and ends on >> {2}'.format(self.title, self.starts_on, self.ends_on)
        

