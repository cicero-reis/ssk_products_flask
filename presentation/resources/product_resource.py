from flask_restful import Resource, request
from marshmallow import ValidationError
from application.product.queries.abstract.get_by_id_product_query_abstract import GetByIdProductQueryAbstract
from application.product.commands.abstract.update_product_command_abstract import UpdateProductCommandAbstract
from application.product.commands.abstract.delete_product_command_abstract import DeleteProductCommandAbstract
from presentation.schemas.product_update_request_schema import ProductUpdateRequestSchema
from presentation.schemas.product_request_schema import ProductRequestSchema
from presentation.schemas.product_response_schema import ProductResponseSchema

class ProductResource(Resource):
    def __init__(self, container):
        self.get_product_by_id_query = container.resolve(GetByIdProductQueryAbstract)
        self.update_product_command = container.resolve(UpdateProductCommandAbstract)
        self.delete_product_command = container.resolve(DeleteProductCommandAbstract)
        self.product_request_schema = ProductRequestSchema()
        self.product_update_request_schema = ProductUpdateRequestSchema()
        self.product_response_schema = ProductResponseSchema()

    def get(self, id):
        product, error = self.get_product_by_id_query.handle(id)
        if error:
            return {'error': error}, 404
        return {'product': product}, 200

    def put(self, id):
        
        json_data = request.json

        if not json_data:
            return {'error': 'No data provided'}, 400

        try:
            data = self.product_request_schema.load(json_data)
        except ValidationError as err:
            return {'error': err.messages}, 400

        product, error = self.update_product_command.handle(id, data)

        if error:
            return {'error': error}, 404

        result = self.product_response_schema.dump(product)
        
        return {'product': result}, 200

    def patch(self, id):

        data = request.json

        if not data:
            return {'error': 'No data provided'}, 400

        try:
            data = self.product_update_request_schema.load(data)
        except ValidationError as e:
            return {'error': e.messages}, 400

        product, error = self.update_product_command.handle(id, data)

        if error:
            return {'error': error}, 404
        
        result = self.product_response_schema.dump(product)

        return {'product': result}, 200

    def delete(self, id):
        success, error = self.delete_product_command.handle(id)
        if error:
            return {'error': error}, 404
        return {'message': 'Product deleted'}, 200
