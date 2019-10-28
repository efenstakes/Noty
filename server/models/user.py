import mongoengine
import datetime
from werkzeug.security import check_password_hash


class User(mongoengine.Document):
    name = mongoengine.StringField( required=True, unique=True, max_length=50 )
    email = mongoengine.EmailField( required=True, unique=True, max_length=50 )
    password = mongoengine.StringField( required=True )
    joined_on = mongoengine.DateTimeField( default=datetime.datetime.utcnow )

    ## define collection name
    meta = { 'collection': 'users' }

    def __repr__(self):
        return 'Im {0} and my email is {1}'.format(self.name, self.email)


    ''' check if a password matches with this objects hashed password '''
    def is_hash_match(self, password):
        return check_password_hash(self.password, password)

    ''' check if name is used '''
    def name_used(self):
        matches = self.objects(name=self.name)
        return len(matches) > 0
    
    ''' check if email is used '''
    def email_used(self):
        matches = self.objects(email=self.email)
        return len(matches) > 0