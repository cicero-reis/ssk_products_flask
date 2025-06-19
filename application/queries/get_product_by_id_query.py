from application.queries.abstract.get_product_by_id_query_abstract import GetProductByIdQueryAbstract
from domain.repositories.get_by_id_product_repository_abstract import GetByIdProductRepositoryAbstract

class GetProductByIdQuery(GetProductByIdQueryAbstract):

    def __init__(self, repo: GetByIdProductRepositoryAbstract):
        self.repo = repo

    def handle(self, id):
        product = self.repo.get_by_id(id)
        if not product:
            return None, f'Product id {id} not found'
        return product.json(), None