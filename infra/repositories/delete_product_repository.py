from infra.models.product_model import ProductModel
from domain.repositories.delete_product_repository_abstract import DeleteProductRepositoryAbstract

class DeleteProductRepository(DeleteProductRepositoryAbstract):
    def delete(self, id):
        product = ProductModel.find_product(id)
        if not product:
            return None
        product.delete_product()
        return product
