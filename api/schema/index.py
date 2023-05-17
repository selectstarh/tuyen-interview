from flask_marshmallow import Schema
from marshmallow.fields import Int, List

class IndexSchema(Schema):
    class Meta:
        fields = ['count', 'lines']

    count = Int()
    lines = List(Int(), required=True)
