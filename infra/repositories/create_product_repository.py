from infra.models.product_model import ProductModel
from domain.repositories.create_product_repository_abstract import CreateProductRepositoryAbstract
from domain.repositories.product_event_store_repository_abstract import ProductEventStoreRepositoryAbstract

class CreateProductRepository(CreateProductRepositoryAbstract):
    def __init__(self, event_store_repo: ProductEventStoreRepositoryAbstract):
        self.event_store_repo = event_store_repo

    def create(self, data):

        product = ProductModel(**data)
        product.save_product()

        event = self.event_store_repo.save_event(
            "ProductCreated",
            product
        )

        return product

