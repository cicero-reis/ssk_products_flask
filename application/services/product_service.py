from domain.repositories.product_repository_abstract import ProductRepositoryAbstract
from application.services.interfaces.product_service_abstract import ProductServiceAbstract

class ProductService(ProductServiceAbstract):

    def __init__(self, repo: ProductRepositoryAbstract):
        self.repo = repo

    def get_all(self):
        products = self.repo.get_all()
        return [product.json() for product in products], None

    def get_by_id(self, id):
        product = self.repo.get_by_id(id)
        if not product:
            return None, f'Product id {id} not found'
        return product.json(), None

    def create(self, data):
        product = self.repo.create(data)
        return product.json(), None

    def update(self, id, data):
        product = self.repo.update(id, data)
        if not product:
            return None, f'Product id {id} not found'
        return product.json(), None

    def delete(self, id):
        product = self.repo.delete(id)
        if not product:
            return None, f'Product id {id} not found'
        return True, None