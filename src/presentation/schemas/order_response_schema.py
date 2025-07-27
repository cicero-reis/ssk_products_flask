from typing import Any
from marshmallow import Schema, fields

class OrderResponseSchema(Schema):
    id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)
