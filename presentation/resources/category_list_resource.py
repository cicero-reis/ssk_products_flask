from flask_restful import Resource, request
from application.category.commands.abstract.create_category_command_abstract import CreateCategoryCommandAbstract
from application.category.queries.abstract.get_all_category_query_abstract import GetAllCategoryQueryAbstract

class CategoryListResource(Resource):
    def __init__(self, container):
        self.create_category_command = container.resolve(CreateCategoryCommandAbstract)
        self.get_all_category_query = container.resolve(GetAllCategoryQueryAbstract)

    def get(self):
        categories, error = self.get_all_category_query.handle()
        if error:
            return {"error": error}, 400
        return {"categories": categories}, 200

    def post(self):
        data = request.json
        category, error = self.create_category_command.handle(data)
        if error:
            return {'error': error}, 400
        return {'category': category}, 201