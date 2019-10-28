import mongoengine
import datetime


class User(mongoengine.Document):
    name = mongoengine.StringField( required=True, unique=True, max_length=50 )
    email = mongoengine.EmailField( required=True, unique=True, max_length=50 )
    password = mongoengine.StringField( required=True )
    joined_on = mongoengine.DateTimeField( default=datetime.datetime.utcnow )

    ## define collection name
    meta = { 'collection': 'users' }

    def __repr__(self):
        return 'Im {0} and my email is {1}'.format(self.name, self.email)

