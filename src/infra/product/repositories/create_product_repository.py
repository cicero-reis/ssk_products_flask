from typing import Any

from src.domain.product.repositories.create_product_repository_abstract import (
    CreateProductRepositoryAbstract,
)
from src.domain.product.repositories.event_product_repository_abstract import (
    EventProductRepositoryAbstract,
)
from src.infra.models.product_model import ProductModel


class CreateProductRepository(CreateProductRepositoryAbstract):
    def __init__(self, event_repo: EventProductRepositoryAbstract) -> Any:
        self.event_repo = event_repo

    def create(self, data: Any) -> Any:
        product = ProductModel(**data)
        product.save_product()

        self.event_repo.save_event("product_created", product)

        return product
