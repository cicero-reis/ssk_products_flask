from flask_restful import Resource, request
from application.services.interfaces.product_service_abstract import ProductServiceAbstract

class ProductListResource(Resource):
    def __init__(self, container):
        self.product_service = container.resolve(ProductServiceAbstract)

    def get(self):
        products, error = self.product_service.get_all()
        if error:
            return {'error': error}, 404
        return {'products': products}, 200

    def post(self):
        data = request.json
        product, error = self.product_service.create(data)
        if error:
            return {'error': error}, 400
        return {'product': product}, 201
