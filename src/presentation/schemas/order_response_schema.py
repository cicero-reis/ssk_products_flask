from typing import Any
from marshmallow import Schema, fields


class ProductResponseSchema(Schema):
    product_id = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)

class OrderResponseSchema(Schema):
    id = fields.Str(required=True)
    order_number = fields.Int(required=True)
    products = fields.List(fields.Nested(ProductResponseSchema), required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
    deleted_at = fields.Raw(allow_none=True)
