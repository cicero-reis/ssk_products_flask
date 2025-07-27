from typing import Any
from src.application.product.dtos.product_dto import ProductDTO
from src.application.product.queries.abstract.get_by_name_product_query_abstract import (
    GetByNameProductQueryAbstract,
)
from src.domain.product.repositories.get_by_name_product_repository_abstract import (
    GetByNameProductRepositoryAbstract,
)


class GetByNameProductQuery(GetByNameProductQueryAbstract):
    def __init__(self, repo: GetByNameProductRepositoryAbstract) -> Any:
        self.repo = repo

    def handle(self, name: Any) -> Any:
        product = self.repo.get_by_name(name)

        if not product:
            return None, f"Product name {name} not found"

        dto = ProductDTO.from_entity(product)

        return dto.to_dict(), None
