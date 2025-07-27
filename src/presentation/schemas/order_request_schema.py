from typing import Any
from marshmallow import Schema, fields, ValidationError


# Schema para um produto individual
class ProductSchema(Schema):
    product_id = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)

# Schema para o pedido, que contém uma lista de produtos e o id do cliente
from marshmallow import validates, ValidationError

class OrderRequestSchema(Schema):
    products = fields.List(fields.Nested(ProductSchema), required=True)

    @validates("products")
    def validate_products(self, value):
        if not value:
            raise ValidationError("A lista de produtos não pode ser vazia.")
