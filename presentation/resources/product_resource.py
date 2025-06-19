from flask_restful import Resource, request
from application.services.interfaces.product_service_abstract import ProductServiceAbstract
from application.queries.abstract.get_product_by_id_query_abstract import GetProductByIdQueryAbstract
from application.commands.abstract.update_product_command_abstract import UpdateProductCommandAbstract
from application.commands.abstract.delete_product_command_abstract import DeleteProductCommandAbstract

class ProductResource(Resource):
    def __init__(self, container):
        self.product_service = container.resolve(ProductServiceAbstract)
        self.get_product_by_id_query = container.resolve(GetProductByIdQueryAbstract)
        self.update_product_command = container.resolve(UpdateProductCommandAbstract)
        self.delete_product_command = container.resolve(DeleteProductCommandAbstract)

    def get(self, id):
        product, error = self.get_product_by_id_query.handle(id)
        if error:
            return {'error': error}, 404
        return {'product': product}, 200

    def put(self, id):
        data = request.json
        product, error = self.update_product_command.handle(id, data)
        if error:
            return {'error': error}, 404
        return {'product': product}, 200

    def delete(self, id):
        success, error = self.delete_product_command.handle(id)
        if error:
            return {'error': error}, 404
        return {'message': 'Product deleted'}, 200
