from infra.models.product_model import ProductModel
from domain.repositories.update_product_repository_abstract import UpdateProductRepositoryAbstract

class UpdateProductRepository(UpdateProductRepositoryAbstract):
    
    def update(self, id, data):
        product = ProductModel.find_product(id)
        if not product:
            return None
        product.update_product(**data)
        return product
