from infra.models.product_model import ProductModel
from domain.repositories.create_product_repository_abstract import CreateProductRepositoryAbstract

class CreateProductRepository(CreateProductRepositoryAbstract):
    def create(self, data):
        product = ProductModel(**data)
        product.save_product()
        return product
