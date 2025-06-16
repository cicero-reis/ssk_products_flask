from flask import Blueprint
from flask_restful import Api
from presentation.resources.product_resource import ProductResource
from presentation.resources.product_list_resource import ProductListResource
from ioc.container import setup_ioc

# Criar o blueprint e API
product_bp = Blueprint('product', __name__)
api = Api(product_bp)

# Configurar IoC container
container = setup_ioc()

# Registrar recursos com IoC
api.add_resource(
    ProductListResource, '/products',
    resource_class_kwargs={'container': container}
)

api.add_resource(
    ProductResource, '/products/<int:id>',
    resource_class_kwargs={'container': container}
)
