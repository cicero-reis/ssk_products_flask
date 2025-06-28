from marshmallow import Schema, fields, validates, validates_schema, ValidationError
from application.product.queries.abstract.get_by_name_product_query_abstract import GetByNameProductQueryAbstract

class ProductPathRequestSchema(Schema):
    id = fields.Integer(required=True, error_messages={"required": "id is required."})
    name = fields.String(required=False, error_messages={"required": "name is required."})
    description = fields.String(required=False, error_messages={"required": "description is required."})
    price = fields.Float(required=False, error_messages={"required": "price is required."})
    category_id = fields.Integer(required=False, error_messages={"required": "category_id is required."})
    image = fields.String(required=False, allow_none=True, error_messages={"required": "image is required."})

    def __init__(self, container, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_by_name_product_query = container.resolve(GetByNameProductQueryAbstract)

    @validates_schema
    def validate_name(self, data, **kwargs):

        current_id = data.get('id')        
        value_name = data.get('name')

        if value_name is not None:
            value_name = value_name.strip()
            
            if not value_name:
                raise ValidationError("name cannot be empty.")

            if len(value_name) < 3:
                raise ValidationError("name must be at least 3 characters long.")

            existing = self.get_by_name_product_query.handle(name=value_name)
            existing_id = existing[0]['id'] if existing and existing[0] else None

            print(f"Validating name: {value_name}, current_id: {current_id}, existing_id: {existing_id}")

            if existing_id is not None and existing_id != current_id:
                    raise ValidationError("name must be unique. This name already exists.")


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