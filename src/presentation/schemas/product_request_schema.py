from typing import Any

from marshmallow import Schema, ValidationError, fields, validates, validates_schema

from src.application.product.queries.abstract.get_by_name_product_query_abstract import (
    GetByNameProductQueryAbstract,
)


class ProductRequestSchema(Schema):
    name = fields.String(required=True, error_messages={"required": "name is required."})
    description = fields.String(
        required=True, error_messages={"required": "description is required."}
    )
    price = fields.Float(required=True, error_messages={"required": "price is required."})
    category_id = fields.Integer(
        required=True, error_messages={"required": "category_id is required."}
    )

    original_name = fields.String(dump_only=True)
    stored_filename = fields.String(dump_only=True)

    def __init__(self, container: Any, *args: Any, **kwargs: Any) -> Any:
        super().__init__(*args, **kwargs)
        self.get_by_name_product_query = container.resolve(GetByNameProductQueryAbstract)

    @validates_schema
    def validate_name(self, data: Any, **kwargs: Any) -> Any:
        current_id = data.get("id")
        value_name = data.get("name")

        if not value_name.strip():
            raise ValidationError("name cannot be empty.")

        if len(value_name) < 3:
            raise ValidationError("name must be at least 3 characters long.")

        existing = self.get_by_name_product_query.handle(name=value_name)
        existing_id = existing[0]["id"] if existing and existing[0] else None

        if existing and existing_id != current_id:
            raise ValidationError("name must be unique. This name already exists.")

    @validates("description")
    def validate_description(self, value: Any) -> Any:
        if not value.strip():
            raise ValidationError("description cannot be empty.")
        if len(value) < 10:
            raise ValidationError("description must be at least 10 characters long.")

    @validates("price")
    def validate_price(self, value: Any) -> Any:
        if value <= 0:
            raise ValidationError("price must be greater than 0.")

    @validates("category_id")
    def validate_category_id(self, value: Any) -> Any:
        if value <= 0:
            raise ValidationError("category_id must be greater than 0.")

    class Meta:
        ordered = True
