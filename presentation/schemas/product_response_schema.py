from marshmallow import Schema, fields

class ProductResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    price = fields.Float()
    category_id = fields.Integer()
    original_name = fields.String()
    stored_filename = fields.String()

    class Meta:
        ordered = True