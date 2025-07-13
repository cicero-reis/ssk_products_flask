from flask_restful import Resource, request
from marshmallow import ValidationError

from src.application.category.commands.abstract.create_category_command_abstract import (
    CreateCategoryCommandAbstract,
)
from src.application.category.queries.abstract.get_all_category_query_abstract import (
    GetAllCategoryQueryAbstract,
)
from src.presentation.schemas.category_request_schema import CategoryRequestSchema
from src.presentation.schemas.category_response_schema import CategoryResponseSchema


class CategoryListResource(Resource):
    def __init__(self, container):
        self.create_category_command = container.resolve(CreateCategoryCommandAbstract)
        self.get_all_category_query = container.resolve(GetAllCategoryQueryAbstract)
        self.category_request_schema = CategoryRequestSchema(container)
        self.category_response_schema = CategoryResponseSchema()

    def get(self):
        categories, error = self.get_all_category_query.handle()
        if error:
            return {"error": error}, 400
        return {"categories": categories}, 200

    def post(self):
        data = request.json

        if not data:
            return {"error": "No data provided"}, 400

        errors = self.category_request_schema.validate(data)

        if errors:
            return {"error": errors}, 400

        try:
            data = self.category_request_schema.load(data)
        except ValidationError as err:
            return {"error": err.messages}, 400

        category, error = self.create_category_command.handle(data)

        if error:
            return {"error": error}, 400

        category = self.category_response_schema.dump(category)

        return {"category": category}, 201
