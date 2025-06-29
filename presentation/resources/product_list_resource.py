from flask_restful import Resource, request
from marshmallow import ValidationError
from utils.file_utils import generate_stored_filename
from utils.upload_to_s3 import upload_to_s3, s3_client
from application.product.queries.abstract.get_all_product_query_abstract import GetAllProductQueryAbstract
from application.product.commands.abstract.create_product_command_abstract import CreateProductCommandAbstract
from presentation.schemas.product_request_schema import ProductRequestSchema
from presentation.schemas.product_response_schema import ProductResponseSchema

class ProductListResource(Resource):
    def __init__(self, container):
        self.get_all_product_query = container.resolve(GetAllProductQueryAbstract)
        self.create_product_command = container.resolve(CreateProductCommandAbstract)
        self.product_request_schema = ProductRequestSchema(container)
        self.product_response_schema = ProductResponseSchema()

    def get(self):
        products, error = self.get_all_product_query.handle()
        if error:
            return {'error': error}, 404
        return {'products': products}, 200

    def post(self):

        form_data = request.form
        
        file = request.files.get('image')

        if not form_data or not file:
            return {'error': 'Dados ou imagem ausente'}, 400

        try:
            data = self.product_request_schema.load(form_data)
        except ValidationError as err:
            return {'error': err.messages}, 400

        original_name = file.filename
        stored_filename = generate_stored_filename(original_name)
        
        try:
            upload_to_s3(file, stored_filename)
        except Exception as e:
            return {'error': f'Erro ao enviar arquivo para S3: {str(e)}'}, 500

        # Adiciona os nomes no payload
        data['original_name'] = original_name
        data['stored_filename'] = stored_filename

        # Chama o comando
        product, error = self.create_product_command.handle(data)

        if error:
            return {'error': error}, 400

        result = self.product_response_schema.dump(product)

        return {'product': result}, 201
