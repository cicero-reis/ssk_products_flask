from flask import Blueprint
from flask_restful import Api

from src.ioc.container import setup_ioc
from src.presentation.resources.order_resource import OrderResource

# Criar o blueprint e API
order_bp = Blueprint("order", __name__)
api = Api(order_bp)

print("Setting up order routes...", order_bp.name)

# Configurar IoC container
container = setup_ioc()

# Registrar recursos com IoC
api.add_resource(OrderResource, "/orders", resource_class_kwargs={"container": container})
