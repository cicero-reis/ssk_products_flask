from marshmallow import Schema, fields

class CategoryResponseSchema(Schema):
    id = fields.Integer(required=True, error_messages={"required": "id is required."})
    name = fields.String(required=True, error_messages={"required": "name is required."})
    description = fields.String(required=True, error_messages={"required": "description is required."})

    class Meta:
        ordered = True