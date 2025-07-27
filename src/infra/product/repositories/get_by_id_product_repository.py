from typing import Any

from src.domain.product.repositories.get_by_id_product_repository_abstract import (
    GetByIdProductRepositoryAbstract,
)
from src.infra.models.product_model import ProductModel


class GetByIdProductRepository(GetByIdProductRepositoryAbstract):
    def get_by_id(self, id: Any) -> Any:
        product = ProductModel.find_product(id)
        if not product:
            return None
        return product
