from flask_restful import Resource, request
from marshmallow import ValidationError
from src.application.product.queries.abstract.get_by_id_product_query_abstract import GetByIdProductQueryAbstract
from src.application.product.commands.abstract.update_product_command_abstract import UpdateProductCommandAbstract
from src.application.product.commands.abstract.delete_product_command_abstract import DeleteProductCommandAbstract
from src.presentation.schemas.product_update_request_schema import ProductUpdateRequestSchema
from src.presentation.schemas.product_path_request_schema import ProductPathRequestSchema
from src.presentation.schemas.product_request_schema import ProductRequestSchema
from src.presentation.schemas.product_response_schema import ProductResponseSchema

class ProductResource(Resource):
    def __init__(self, container):
        self.get_product_by_id_query = container.resolve(GetByIdProductQueryAbstract)
        self.update_product_command = container.resolve(UpdateProductCommandAbstract)
        self.delete_product_command = container.resolve(DeleteProductCommandAbstract)
        self.product_request_schema = ProductRequestSchema(container)
        self.product_update_request_schema = ProductUpdateRequestSchema(container)
        self.product_path_request_schema = ProductPathRequestSchema(container)
        self.product_response_schema = ProductResponseSchema()

    def get(self, id):
        product, error = self.get_product_by_id_query.handle(id)
        if error:
            return {'error': error}, 404
        return {'product': product}, 200

    def put(self, id):
        
        data = request.json

        if not data:
            return {'error': 'No data provided'}, 400        

        try:
            data = self.product_update_request_schema.load(data)
        except ValidationError as err:
            return {'error': err.messages}, 400

        if id != data['id']:
            return {'error': 'Data invalid'}, 400

        product, error = self.update_product_command.handle(id, data)

        if error:
            return {'error': error}, 404

        product = self.product_response_schema.dump(product)
        
        return {'product': product}, 200

    def patch(self, id):

        data = request.json

        if not data:
            return {'error': 'No data provided'}, 400        

        try:
            data = self.product_path_request_schema.load(data)
        except ValidationError as e:
            return {'error': e.messages}, 400

        if id != data['id']:
            return {'error': 'Data invalid'}, 400

        product, error = self.update_product_command.handle(id, data)

        if error:
            return {'error': error}, 404
        
        product = self.product_response_schema.dump(product)

        return {'product': product}, 200

    def delete(self, id):
        success, error = self.delete_product_command.handle(id)
        if error:
            return {'error': error}, 404
        return {'message': 'Product deleted'}, 200
