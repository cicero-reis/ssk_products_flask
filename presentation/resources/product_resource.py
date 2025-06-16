from flask_restful import Resource, request
from application.services.interfaces.product_service_abstract import ProductServiceAbstract

class ProductResource(Resource):
    def __init__(self, container):
        self.product_service = container.resolve(ProductServiceAbstract)

    def get(self, id):
        product, error = self.product_service.get_by_id(id)
        if error:
            return {'error': error}, 404
        return {'product': product}, 200

    def put(self, id):
        data = request.json
        product, error = self.product_service.update(id, data)
        if error:
            return {'error': error}, 404
        return {'product': product}, 200

    def delete(self, id):
        success, error = self.product_service.delete(id)
        if error:
            return {'error': error}, 404
        return {'message': 'Product deleted'}, 200
