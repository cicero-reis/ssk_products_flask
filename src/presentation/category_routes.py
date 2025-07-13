from flask import Blueprint
from flask_restful import Api
from src.presentation.resources.category_list_resource import CategoryListResource
from src.presentation.resources.category_resource import CategoryResource
from src.ioc.container import setup_ioc

category_bp = Blueprint('category', __name__)
api = Api(category_bp)

print('Setting up category routes...', category_bp.name)

container = setup_ioc()

api.add_resource(
    CategoryListResource, '/categories',
    resource_class_kwargs={'container': container}
)

api.add_resource(
    CategoryResource, '/categories/<int:id>',
    resource_class_kwargs={'container': container}
)
