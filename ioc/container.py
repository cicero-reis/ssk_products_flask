from infra.repositories.get_all_product_repository import GetAllProductRepository
from application.queries.get_all_product_query import GetAllProductQuery
from application.queries.abstract.get_all_product_query_abstract import GetAllProductQueryAbstract

from infra.repositories.get_by_id_product_repository import GetByIdProductRepository
from application.queries.get_product_by_id_query import GetProductByIdQuery
from application.queries.abstract.get_product_by_id_query_abstract import GetProductByIdQueryAbstract

from infra.repositories.create_product_repository import CreateProductRepository
from application.commands.create_product_command import CreateProductCommand
from application.commands.abstract.create_product_command_abstract import CreateProductCommandAbstract

from infra.repositories.update_product_repository import UpdateProductRepository
from application.commands.update_product_command import UpdateProductCommand
from application.commands.abstract.update_product_command_abstract import UpdateProductCommandAbstract

from infra.repositories.delete_product_repository import DeleteProductRepository
from application.commands.delete_product_command import DeleteProductCommand
from application.commands.abstract.delete_product_command_abstract import DeleteProductCommandAbstract

from application.events.event_publisher import EventPublisher
from application.events.abstract.event_publisher_abstract import EventPublisherAbstract

from infra.repositories.product_event_store_repository import ProductEventStoreRepository


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
    
    get_all_product_repo = GetAllProductRepository()
    get_all_product_query = GetAllProductQuery(get_all_product_repo)

    get_by_id_product_repo = GetByIdProductRepository()
    get_product_by_id_query = GetProductByIdQuery(get_by_id_product_repo)

    product_event_store_repo = ProductEventStoreRepository()

    create_product_repo = CreateProductRepository(product_event_store_repo)
    event_publisher = EventPublisher()
    create_product_command = CreateProductCommand(create_product_repo, event_publisher)

    update_product_repo = UpdateProductRepository(product_event_store_repo)
    update_product_command = UpdateProductCommand(update_product_repo)

    delete_product_repo = DeleteProductRepository(product_event_store_repo)
    delete_product_command = DeleteProductCommand(delete_product_repo)

    # Criar e registrar no container
    container = IoCContainer()    
    container.register(GetAllProductQueryAbstract, get_all_product_query)
    container.register(GetProductByIdQueryAbstract, get_product_by_id_query)
    container.register(CreateProductCommandAbstract, create_product_command)
    container.register(UpdateProductCommandAbstract, update_product_command)
    container.register(DeleteProductCommandAbstract, delete_product_command)

    return container
