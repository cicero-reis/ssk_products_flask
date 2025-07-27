from typing import Any

from src.domain.product.repositories.get_by_name_product_repository_abstract import (
    GetByNameProductRepositoryAbstract,
)
from src.infra.models.product_model import ProductModel


class GetByNameProductRepository(GetByNameProductRepositoryAbstract):
    def get_by_name(self, name: Any) -> Any:
        product = ProductModel.find_by_name(name)

        if not product:
            return None

        return product
