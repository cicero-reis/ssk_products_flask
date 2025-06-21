from infra.product.repositories.get_all_product_repository import GetAllProductRepository
from application.product.queries.get_all_product_query import GetAllProductQuery
from application.product.queries.abstract.get_all_product_query_abstract import GetAllProductQueryAbstract

from infra.product.repositories.get_by_id_product_repository import GetByIdProductRepository
from application.product.queries.get_product_by_id_query import GetProductByIdQuery
from application.product.queries.abstract.get_product_by_id_query_abstract import GetProductByIdQueryAbstract

from infra.product.repositories.create_product_repository import CreateProductRepository
from application.product.commands.create_product_command import CreateProductCommand
from application.product.commands.abstract.create_product_command_abstract import CreateProductCommandAbstract

from infra.product.repositories.update_product_repository import UpdateProductRepository
from application.product.commands.update_product_command import UpdateProductCommand
from application.product.commands.abstract.update_product_command_abstract import UpdateProductCommandAbstract

from infra.product.repositories.delete_product_repository import DeleteProductRepository
from application.product.commands.delete_product_command import DeleteProductCommand
from application.product.commands.abstract.delete_product_command_abstract import DeleteProductCommandAbstract

from application.product.events.event_product_publisher import EventProductPublisher

from infra.product.repositories.event_product_repository import EventProductRepository


class IoCContainer:
    def __init__(self):
        self._services = {}

    def register(self, abstract_type, instance):
        """Registra um serviço instanciado para um tipo abstrato"""
        self._services[abstract_type] = instance

    def resolve(self, abstract_type):
        """Obtém o serviço registrado para o tipo abstrato"""
        service = self._services.get(abstract_type)
        if service is None:
            raise Exception(f"Serviço não registrado para {abstract_type}")
        return service

def setup_ioc():
    
    event_publisher = EventProductPublisher()
    event_product_repo = EventProductRepository()

    get_all_product_repo = GetAllProductRepository()
    get_all_product_query = GetAllProductQuery(get_all_product_repo)

    get_by_id_product_repo = GetByIdProductRepository()
    get_product_by_id_query = GetProductByIdQuery(get_by_id_product_repo)

    create_product_repo = CreateProductRepository(event_product_repo)

    create_product_command = CreateProductCommand(create_product_repo, event_publisher)

    update_product_repo = UpdateProductRepository(event_product_repo)
    update_product_command = UpdateProductCommand(update_product_repo)

    delete_product_repo = DeleteProductRepository(event_product_repo)
    delete_product_command = DeleteProductCommand(delete_product_repo)

    # Criar e registrar no container
    container = IoCContainer()    
    container.register(GetAllProductQueryAbstract, get_all_product_query)
    container.register(GetProductByIdQueryAbstract, get_product_by_id_query)
    container.register(CreateProductCommandAbstract, create_product_command)
    container.register(UpdateProductCommandAbstract, update_product_command)
    container.register(DeleteProductCommandAbstract, delete_product_command)

    return container
