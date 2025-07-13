from src.application.product.dtos.product_dto import ProductDTO
from src.application.product.queries.abstract.get_all_product_query_abstract import (
    GetAllProductQueryAbstract,
)
from src.domain.product.repositories.get_all_product_repository_abstract import (
    GetAllProductRepositoryAbstract,
)


class GetAllProductQuery(GetAllProductQueryAbstract):
    def __init__(self, repo: GetAllProductRepositoryAbstract):
        self.repo = repo

    def handle(self):
        products = self.repo.get_all()
        dtos = [ProductDTO.from_entity(p).to_dict() for p in products]
        return dtos, None
