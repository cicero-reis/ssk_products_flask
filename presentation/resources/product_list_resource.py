from flask_restful import Resource, request
from marshmallow import ValidationError
from application.product.queries.abstract.get_all_product_query_abstract import GetAllProductQueryAbstract
from application.product.commands.abstract.create_product_command_abstract import CreateProductCommandAbstract
from presentation.schemas.product_request_schema import ProductRequestSchema
from presentation.schemas.product_response_schema import ProductResponseSchema

class ProductListResource(Resource):
    def __init__(self, container):
        self.get_all_product_query = container.resolve(GetAllProductQueryAbstract)
        self.create_product_command = container.resolve(CreateProductCommandAbstract)
        self.product_request_schema = ProductRequestSchema()
        self.product_response_schema = ProductResponseSchema()

    def get(self):
        products, error = self.get_all_product_query.handle()
        if error:
            return {'error': error}, 404
        return {'products': products}, 200

    def post(self):
        
        json_data = request.json
        
        if not json_data:
            return {'error': 'No data provided'}, 400

        try:
            data = self.product_request_schema.load(json_data)
        except ValidationError as err:
            return {'error': err.messages}, 400

        product, error = self.create_product_command.handle(data)
        
        if error:
            return {'error': error}, 400

        result = self.product_response_schema.dump(product)

        return {'product': result}, 201
