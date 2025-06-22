from infra.models.product_model import ProductModel
from domain.product.repositories.create_product_repository_abstract import CreateProductRepositoryAbstract
from domain.product.repositories.event_product_repository_abstract import EventProductRepositoryAbstract

class CreateProductRepository(CreateProductRepositoryAbstract):
    def __init__(self, event_repo: EventProductRepositoryAbstract):
        self.event_repo = event_repo

    def create(self, data):
        
        product = ProductModel(**data)
        product.save_product()

        self.event_repo.save_event("ProductCreated", product)

        return product

