from typing import Any
from marshmallow import Schema, ValidationError, fields, validates, validates_schema

from src.application.category.queries.abstract.get_by_name_category_query_abstract import (
    GetByNameCategoryQueryAbstract,
)


class CategoryPatchRequestSchema(Schema):
    id = fields.Integer(required=True, error_messages={"required": "id is required."})
    name = fields.String(required=False, error_messages={"required": "name is required."})
    description = fields.String(
        required=False, error_messages={"required": "description is required."}
    )

    def __init__(self, container: Any, *args: Any, **kwargs: Any) -> Any:
        super().__init__(*args, **kwargs)
        self.get_by_name_category_query = container.resolve(GetByNameCategoryQueryAbstract)

    @validates_schema
    def validate_name(self, data: Any, **kwargs: Any) -> Any:
        current_id = data.get("id")
        value_name = data.get("name")

        if value_name is not None:
            value_name = value_name.strip()

            if not value_name:
                raise ValidationError("name cannot be empty.")

            if len(value_name) < 3:
                raise ValidationError("name must be at least 3 characters long.")

            existing = self.get_by_name_category_query.handle(name=value_name)
            existing_id = existing[0]["id"] if existing and existing[0] else None

            if existing_id is not None and existing_id != current_id:
                raise ValidationError("name must be unique. This name already exists.")

    @validates("description")
    def validate_description(self, value: Any) -> Any:
        if value is not None:
            if not value.strip():
                raise ValidationError("description cannot be empty.")
            if len(value.strip()) < 10:
                raise ValidationError("description must be at least 10 characters long.")

    class Meta:
        ordered = True
