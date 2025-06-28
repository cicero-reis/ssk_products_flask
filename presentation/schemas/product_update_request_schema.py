from marshmallow import Schema, fields, validates, ValidationError

class ProductUpdateRequestSchema(Schema):
    name = fields.String(required=False, error_messages={"required": "name is required."})
    description = fields.String(required=False, error_messages={"required": "description is required."})
    price = fields.Float(required=False, error_messages={"required": "price is required."})
    category_id = fields.Integer(required=False, error_messages={"required": "category_id is required."})
    image = fields.String(required=False, allow_none=True, error_messages={"required": "image is required."})

    @validates('name')
    def validate_name(self, value):
        if value is not None:
            if not value.strip():
                raise ValidationError("name cannot be empty.")
            if len(value.strip()) < 3:
                raise ValidationError("name must be at least 3 characters long.")

    @validates('description')
    def validate_description(self, value):
        if value is not None:
            if not value.strip():
                raise ValidationError("description cannot be empty.")
            if len(value.strip()) < 10:
                raise ValidationError("description must be at least 10 characters long.")

    @validates('price')
    def validate_price(self, value):
        if value is not None and value <= 0:
            raise ValidationError("price must be greater than 0.")

    @validates('category_id')
    def validate_category_id(self, value):
        if value is not None and value <= 0:
            raise ValidationError("category_id must be greater than 0.")

    class Meta:
        ordered = True