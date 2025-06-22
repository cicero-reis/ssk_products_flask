from flask_restful import Resource, request
from application.category.commands.abstract.delete_category_command_abstract import DeleteCategoryCommandAbstract
from application.category.queries.abstract.get_by_id_category_query_abstract import GetByIdCategoryQueryAbstract
from application.category.commands.abstract.update_category_command_abstract import UpdateCategoryCommandAbstract

class CategoryResource(Resource):
    def __init__(self, container):
        self.delete_category_command = container.resolve(DeleteCategoryCommandAbstract)
        self.get_by_id_category_query = container.resolve(GetByIdCategoryQueryAbstract)
        self.update_category_command = container.resolve(UpdateCategoryCommandAbstract)

    def get(self, id):
        category, error = self.get_by_id_category_query.handle(id)
        if error:
            return {"error": error}, 404
        return {'category': category}, 200

    def put(self, id):
        data = request.json
        category, error = self.update_category_command.handle(id, data)
        if error:
            return {"error": error}, 400
        return {'category': category}, 200

    

    def delete(self, id):
        success, error = self.delete_category_command.handle(id)
        if error:
            return {"error": error}, 404
        return {"category": "Category deleted"}, 200
    