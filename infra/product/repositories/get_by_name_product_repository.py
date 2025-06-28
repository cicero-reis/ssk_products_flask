from infra.models.product_model import ProductModel
from domain.product.repositories.get_by_name_product_repository_abstract import GetByNameProductRepositoryAbstract

class GetByNameProductRepository(GetByNameProductRepositoryAbstract):
    
    def get_by_name(self, name):

        product = ProductModel.find_by_name(name)

        if not product:
            return None

        return product
