from typing import Any

from src.domain.product.repositories.event_product_repository_abstract import (
    EventProductRepositoryAbstract,
)
from src.domain.product.repositories.update_product_repository_abstract import (
    UpdateProductRepositoryAbstract,
)
from src.infra.models.product_model import ProductModel


class UpdateProductRepository(UpdateProductRepositoryAbstract):
    def __init__(self, event_repo: EventProductRepositoryAbstract) -> Any:
        self.event_repo = event_repo

    def update(self, id: Any, data: Any) -> Any:
        product = ProductModel.find_product(id)
        if not product:
            return None
        product.update_product(**data)

        self.event_repo.save_event("product_updated", product)

        return True, product
