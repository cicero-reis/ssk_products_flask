from infra.repositories.product_repository import ProductRepository
from application.services.product_service import ProductService
from application.services.interfaces.product_service_abstract import ProductServiceAbstract

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
    # Instanciar repositórios
    product_repository = ProductRepository()

    # Instanciar serviços com as dependências
    product_service = ProductService(product_repository)

    # Criar e registrar no container
    container = IoCContainer()
    container.register(ProductServiceAbstract, product_service)

    return container
