from src.domain.product.repositories.delete_product_repository_abstract import (
    DeleteProductRepositoryAbstract,
)
from src.domain.product.repositories.event_product_repository_abstract import (
    EventProductRepositoryAbstract,
)
from src.infra.models.product_model import ProductModel


class DeleteProductRepository(DeleteProductRepositoryAbstract):
    def __init__(self, event_repo: EventProductRepositoryAbstract):
        self.event_repo = event_repo

    def delete(self, id):
        product = ProductModel.find_product(id)
        if not product:
            return None
        product.delete_product()

        self.event_repo.save_event("product_deleted", product)

        return product
