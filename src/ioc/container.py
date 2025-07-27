from typing import Any

from src.application.category.commands.abstract.create_category_command_abstract import (
    CreateCategoryCommandAbstract,
)
from src.application.category.commands.abstract.delete_category_command_abstract import (
    DeleteCategoryCommandAbstract,
)
from src.application.category.commands.abstract.update_category_command_abstract import (
    UpdateCategoryCommandAbstract,
)

# category commands
from src.application.category.commands.create_category_command import CreateCategoryCommand
from src.application.category.commands.delete_category_command import DeleteCategoryCommand
from src.application.category.commands.update_category_command import UpdateCategoryCommand
from src.application.category.events.event_category_publisher import EventCategoryPublisher
from src.application.category.queries.abstract.get_all_category_query_abstract import (
    GetAllCategoryQueryAbstract,
)
from src.application.category.queries.abstract.get_by_id_category_query_abstract import (
    GetByIdCategoryQueryAbstract,
)
from src.application.category.queries.abstract.get_by_name_category_query_abstract import (
    GetByNameCategoryQueryAbstract,
)

# category queries
from src.application.category.queries.get_all_category_query import GetAllCategoryQuery
from src.application.category.queries.get_by_id_category_query import GetByIdCategoryQuery
from src.application.category.queries.get_by_name_category_query import GetByNameCategoryQuery
from src.application.order.commands.abstract.create_order_command_abstract import (
    CreateOrderCommandAbstract,
)
from src.application.order.commands.abstract.delete_order_command_abstract import (
    DeleteOrderCommandAbstract,
)
from src.application.order.commands.abstract.update_order_command_abstract import (
    UpdateOrderCommandAbstract,
)

# order commands
from src.application.order.commands.create_order_command import CreateOrderCommand
from src.application.order.commands.delete_order_command import DeleteOrderCommand
from src.application.order.commands.update_order_command import UpdateOrderCommand
from src.application.order.queries.abstract.get_all_order_query_abstract import (
    GetAllOrderQueryAbstract,
)
from src.application.order.queries.abstract.get_by_id_order_query_abstract import (
    GetByIdOrderQueryAbstract,
)

# order queries
from src.application.order.queries.get_all_order_query import GetAllOrderQuery
from src.application.order.queries.get_by_id_order_query import GetByIdOrderQuery
from src.application.product.commands.abstract.create_product_command_abstract import (
    CreateProductCommandAbstract,
)
from src.application.product.commands.abstract.delete_product_command_abstract import (
    DeleteProductCommandAbstract,
)
from src.application.product.commands.abstract.update_product_command_abstract import (
    UpdateProductCommandAbstract,
)

# product commands
from src.application.product.commands.create_product_command import CreateProductCommand
from src.application.product.commands.delete_product_command import DeleteProductCommand
from src.application.product.commands.update_product_command import UpdateProductCommand

# product events
from src.application.product.events.event_product_publisher import EventProductPublisher
from src.application.product.queries.abstract.get_all_product_query_abstract import (
    GetAllProductQueryAbstract,
)
from src.application.product.queries.abstract.get_by_id_product_query_abstract import (
    GetByIdProductQueryAbstract,
)
from src.application.product.queries.abstract.get_by_name_product_query_abstract import (
    GetByNameProductQueryAbstract,
)

# product queries
from src.application.product.queries.get_all_product_query import GetAllProductQuery
from src.application.product.queries.get_by_id_product_query import GetByIdProductQuery
from src.application.product.queries.get_by_name_product_query import GetByNameProductQuery

# category repositories
from src.infra.category.repositories.create_category_repository import CreateCategoryRepository
from src.infra.category.repositories.delete_category_repository import DeleteCategoryRepository

# category events
from src.infra.category.repositories.event_category_repository import EventCategoryRepository
from src.infra.category.repositories.get_all_category_repository import GetAllCategoryRepository
from src.infra.category.repositories.get_by_id_category_repository import GetByIdCategoryRepository
from src.infra.category.repositories.get_by_name_category_repository import (
    GetByNameCategoryRepository,
)
from src.infra.category.repositories.update_category_repository import UpdateCategoryRepository

# order repositories
from src.infra.order.repositories.create_order_repository import CreateOrderRepository
from src.infra.order.repositories.delete_order_repository import DeleteOrderRepository
from src.infra.order.repositories.get_all_order_repository import GetAllOrderRepository
from src.infra.order.repositories.get_by_id_order_repository import GetByIdOrderRepository
from src.infra.order.repositories.update_order_repository import UpdateOrderRepository

# product repositories
from src.infra.product.repositories.create_product_repository import CreateProductRepository
from src.infra.product.repositories.delete_product_repository import DeleteProductRepository
from src.infra.product.repositories.event_product_repository import EventProductRepository
from src.infra.product.repositories.get_all_product_repository import GetAllProductRepository
from src.infra.product.repositories.get_by_id_product_repository import GetByIdProductRepository
from src.infra.product.repositories.get_by_name_product_repository import GetByNameProductRepository
from src.infra.product.repositories.update_product_repository import UpdateProductRepository

# s3 service
from src.services.interfaces.i_s3_service import IS3Service
from src.services.s3_service import S3Service


class IoCContainer:
    def __init__(self) -> Any:
        self._services = {}

    def register(self, abstract_type: Any, instance: Any) -> Any:
        """Registra um serviço instanciado para um tipo abstrato"""
        self._services[abstract_type] = instance

    def resolve(self, abstract_type: Any) -> Any:
        """Obtém o serviço registrado para o tipo abstrato"""
        service = self._services.get(abstract_type)
        if service is None:
            raise ValueError(f"Serviço não registrado para {abstract_type}")
        return service


def setup_ioc() -> Any:
    # Product
    event_publisher_product = EventProductPublisher()
    event_product_repo = EventProductRepository()
    get_all_product_repo = GetAllProductRepository()
    get_all_product_query = GetAllProductQuery(get_all_product_repo)
    get_by_id_product_repo = GetByIdProductRepository()
    get_product_by_id_query = GetByIdProductQuery(get_by_id_product_repo)
    get_by_name_product_repo = GetByNameProductRepository()
    get_by_name_product_query = GetByNameProductQuery(get_by_name_product_repo)
    create_product_repo = CreateProductRepository(event_product_repo)
    create_product_command = CreateProductCommand(create_product_repo, event_publisher_product)
    update_product_repo = UpdateProductRepository(event_product_repo)
    update_product_command = UpdateProductCommand(update_product_repo, event_publisher_product)
    delete_product_repo = DeleteProductRepository(event_product_repo)
    delete_product_command = DeleteProductCommand(delete_product_repo, event_publisher_product)

    # Order
    # (event_publisher_order e event_order_repo podem ser implementados depois, se necessário)
    get_all_order_repo = GetAllOrderRepository()
    get_all_order_query = GetAllOrderQuery(get_all_order_repo)
    get_by_id_order_repo = GetByIdOrderRepository()
    get_by_id_order_query = GetByIdOrderQuery(get_by_id_order_repo)
    create_order_repo = CreateOrderRepository()
    create_order_command = CreateOrderCommand(create_order_repo, None)
    update_order_repo = UpdateOrderRepository()
    update_order_command = UpdateOrderCommand(update_order_repo, None)
    delete_order_repo = DeleteOrderRepository()
    delete_order_command = DeleteOrderCommand(delete_order_repo, None)

    # Category
    event_publisher_category = EventCategoryPublisher()
    event_category_repo = EventCategoryRepository()
    get_all_category_repo = GetAllCategoryRepository()
    get_all_category_query = GetAllCategoryQuery(get_all_category_repo)
    get_by_id_category_repo = GetByIdCategoryRepository()
    get_by_id_category_query = GetByIdCategoryQuery(get_by_id_category_repo)
    create_category_repo = CreateCategoryRepository(event_category_repo)
    create_category_command = CreateCategoryCommand(create_category_repo, event_publisher_category)
    update_category_repo = UpdateCategoryRepository(event_category_repo)
    update_category_command = UpdateCategoryCommand(update_category_repo, event_publisher_category)
    delete_category_repo = DeleteCategoryRepository(event_category_repo)
    delete_category_command = DeleteCategoryCommand(delete_category_repo, event_publisher_category)
    get_by_name_category_repo = GetByNameCategoryRepository()
    get_by_name_category_query = GetByNameCategoryQuery(get_by_name_category_repo)

    # S3 Service
    s3_service = S3Service()

    # Criar e registrar no container
    container = IoCContainer()

    # S3 Service
    container.register(IS3Service, s3_service)

    # Product
    container.register(GetAllProductQueryAbstract, get_all_product_query)
    container.register(GetByIdProductQueryAbstract, get_product_by_id_query)
    container.register(GetByNameProductQueryAbstract, get_by_name_product_query)
    container.register(CreateProductCommandAbstract, create_product_command)
    container.register(UpdateProductCommandAbstract, update_product_command)
    container.register(DeleteProductCommandAbstract, delete_product_command)

    # Order
    container.register(GetAllOrderQueryAbstract, get_all_order_query)
    container.register(GetByIdOrderQueryAbstract, get_by_id_order_query)
    container.register(CreateOrderCommandAbstract, create_order_command)
    container.register(UpdateOrderCommandAbstract, update_order_command)
    container.register(DeleteOrderCommandAbstract, delete_order_command)

    # Category
    container.register(GetAllCategoryQueryAbstract, get_all_category_query)
    container.register(GetByIdCategoryQueryAbstract, get_by_id_category_query)
    container.register(CreateCategoryCommandAbstract, create_category_command)
    container.register(UpdateCategoryCommandAbstract, update_category_command)
    container.register(DeleteCategoryCommandAbstract, delete_category_command)
    container.register(GetByNameCategoryQueryAbstract, get_by_name_category_query)

    return container
