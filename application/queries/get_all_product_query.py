from application.queries.abstract.get_all_product_query_abstract import GetAllProductQueryAbstract
from domain.repositories.get_all_product_repository_abstract import GetAllProductRepositoryAbstract

class GetAllProductQuery(GetAllProductQueryAbstract):

    def __init__(self, repo: GetAllProductRepositoryAbstract):
        self.repo = repo

    def handle(self):
        products = self.repo.get_all()
        return [product.json() for product in products], None