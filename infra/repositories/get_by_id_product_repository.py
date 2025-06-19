from infra.models.product_model import ProductModel
from domain.repositories.get_by_id_product_repository_abstract import GetByIdProductRepositoryAbstract

class GetByIdProductRepository(GetByIdProductRepositoryAbstract):
    
    def get_by_id(self, id):
        product = ProductModel.find_product(id)
        if not product:
            return None
        return product
