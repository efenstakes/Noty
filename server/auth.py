from app import jwt
import mongoengine
from models import User

''' message to show if jwt authorization fails '''
@jwt.unauthorized_loader
def unauthorized_loader_callback(reason):
    return { 'error': 'Authentication Failed', 'reason': reason }, 401

''' message to show if jwt token is invalid '''
@jwt.invalid_token_loader
def invalid_token_loader_callback(reason):
    return { 'error': 'Authentication Failed', 'reason': reason }, 401

''' message to show if jwt token is expired '''
@jwt.expired_token_loader
def expired_token_loader_callback(reason):
    return { 'error': 'Authentication Failed' }, 401


# This function is called whenever a protected endpoint is accessed,
# and must return an object based on the tokens identity.
# This is called after the token is verified, so you can use
# get_jwt_claims() in here if desired. Note that this needs to
# return None if the user could not be loaded for any reason,
# such as not being found in the underlying data store
@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    try:
        user = User.objects(id=identity).get()
    except ( mongoengine.errors.ValidationError, mongoengine.errors.DoesNotExist ):
        return None
        
    print('got user {}'.format(user.email))
    return user 


# You can override the error returned to the user if the
# user_loader_callback returns None. If you don't override
# this, # it will return a 401 status code with the JSON:
# {"msg": "Error loading the user <identity>"}.
# You can use # get_jwt_claims() here too if desired
@jwt.user_loader_error_loader
def custom_user_loader_error_callback(identity):
    return { "error": "User Authentication Error" }, 401

# Using the expired_token_loader decorator, we will now call
# this function whenever an expired but otherwise valid access
# token attempts to access an endpoint
@jwt.expired_token_loader
def jwt_expired_token_callback(expired_token):
    return { 'error': 'Expired Authentication Token Provided' }, 401

