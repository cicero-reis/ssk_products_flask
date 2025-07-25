from src.application.product.dtos.product_dto import ProductDTO
from src.application.product.queries.abstract.get_by_id_product_query_abstract import (
    GetByIdProductQueryAbstract,
)
from src.domain.product.repositories.get_by_id_product_repository_abstract import (
    GetByIdProductRepositoryAbstract,
)


class GetByIdProductQuery(GetByIdProductQueryAbstract):
    def __init__(self, repo: GetByIdProductRepositoryAbstract):
        self.repo = repo

    def handle(self, id):
        product = self.repo.get_by_id(id)
        if not product:
            return None, f"Product id {id} not found"

        dto = ProductDTO.from_entity(product)
        return dto.to_dict(), None
