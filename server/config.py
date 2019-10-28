import os

class Config(object):
    TESTING = os.environ.get('TESTING')
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    ## so reqparser returns all errors rather than the first
    BUNDLE_ERRORS = os.environ.get('BUNDLE_ERRORS')


