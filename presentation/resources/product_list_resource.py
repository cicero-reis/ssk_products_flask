from flask_restful import Resource, request
from application.product.queries.abstract.get_all_product_query_abstract import GetAllProductQueryAbstract
from application.product.commands.abstract.create_product_command_abstract import CreateProductCommandAbstract

class ProductListResource(Resource):
    def __init__(self, container):
        self.get_all_product_query = container.resolve(GetAllProductQueryAbstract)
        self.create_product_command = container.resolve(CreateProductCommandAbstract)

    def get(self):
        products, error = self.get_all_product_query.handle()
        if error:
            return {'error': error}, 404
        return {'products': products}, 200

    def post(self):
        data = request.json
        product, error = self.create_product_command.handle(data)
        if error:
            return {'error': error}, 400
        return {'product': product}, 201
