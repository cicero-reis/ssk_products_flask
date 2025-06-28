from flask_restful import Resource, request
from marshmallow import ValidationError
from application.category.commands.abstract.delete_category_command_abstract import DeleteCategoryCommandAbstract
from application.category.queries.abstract.get_by_id_category_query_abstract import GetByIdCategoryQueryAbstract
from application.category.commands.abstract.update_category_command_abstract import UpdateCategoryCommandAbstract
from presentation.schemas.category_update_request_schema import CategoryUpdateRequestSchema
from presentation.schemas.category_response_schema import CategoryResponseSchema
from presentation.schemas.category_patch_request_schema import CategoryPatchRequestSchema

class CategoryResource(Resource):
    def __init__(self, container):
        self.delete_category_command = container.resolve(DeleteCategoryCommandAbstract)
        self.get_by_id_category_query = container.resolve(GetByIdCategoryQueryAbstract)
        self.update_category_command = container.resolve(UpdateCategoryCommandAbstract)
        self.category_update_request_schema = CategoryUpdateRequestSchema(container)
        self.category_response_schema = CategoryResponseSchema()
        self.category_patch_request_schema = CategoryPatchRequestSchema(container)

    def get(self, id):
        category, error = self.get_by_id_category_query.handle(id)
        if error:
            return {"error": error}, 404
        return {'category': category}, 200

    def put(self, id):
        
        data = request.json

        if not data:
            return {'error': 'No data provided'}, 400

        print (f"Received data for update: {data['id']} for category ID: {id}")

        if id != data['id']:
            return {'error': 'Data invalid'}, 400

        try:
            data = self.category_update_request_schema.load(data)
        except ValidationError as err:
            return {'error': err.messages}, 400

        category, error = self.update_category_command.handle(id, data)
        
        if error:
            return {"error": error}, 400

        category = self.category_response_schema.dump(category)

        return {'category': category}, 200

    def patch(self, id):

        data = request.json

        if not data:
            return {'error': 'No data provided'}, 400

        if id != data['id']:
            return {'error': 'Data invalid'}, 400

        try:
            data = self.category_patch_request_schema.load(data)
        except ValidationError as e:
            return {'error': e.messages}, 400

        category, error = self.update_category_command.handle(id, data)

        if error:
            return {"error": error}, 404

        result = self.category_response_schema.dump(category)

        return {'category': result}, 200

    def delete(self, id):

        success, error = self.delete_category_command.handle(id)

        if error:
            return {"error": error}, 404
            
        return {"category": "Category deleted"}, 200
    