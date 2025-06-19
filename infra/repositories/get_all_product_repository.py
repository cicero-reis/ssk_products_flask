from infra.models.product_model import ProductModel
from domain.repositories.get_all_product_repository_abstract import GetAllProductRepositoryAbstract

class GetAllProductRepository(GetAllProductRepositoryAbstract):

    def get_all(self):
        products = ProductModel.get_all_active_products()
        return products
