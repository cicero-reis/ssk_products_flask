from marshmallow import Schema, fields

class ProductResponseSchema(Schema):
    id = fields.Integer(required=True, error_messages={"required": "id is required."})
    name = fields.String(required=True, error_messages={"required": "name is required."})
    description = fields.String(required=True, error_messages={"required": "description is required."})
    price = fields.Float(required=True, error_messages={"required": "price is required."})
    category_id = fields.Integer(required=True, error_messages={"required": "category_id is required."})    

    class Meta:
        ordered = True