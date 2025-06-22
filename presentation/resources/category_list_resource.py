from flask_restful import Resource, request
from application.category.commands.abstract.create_category_command_abstract import CreateCategoryCommandAbstract

class CategoryListResource(Resource):
    def __init__(self, container):
        self.create_category_command = container.resolve(CreateCategoryCommandAbstract)

    def post(self):
        data = request.json
        category, error = self.create_category_command.handle(data)
        if error:
            return {'error': error}, 400
        return {'category': category}, 201