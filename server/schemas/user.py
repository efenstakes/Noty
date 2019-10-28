from app import ma 
from marshmallow import fields


class UserSchema(ma.Schema):
    id = fields.String()
    class Meta:
        additional = ( 'name', 'email', 'joined_on' )