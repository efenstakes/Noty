from app import ma 
from marshmallow import fields


class TaskSchema(ma.Schema):
    id = fields.String()
    class Meta:
        additional = ( 
            'title', 'body', 'stage', 'starts_on', 'ends_on', 
            'added_on', 'participants' 
        )
        