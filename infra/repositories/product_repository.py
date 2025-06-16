from infra.models.product_model import ProductModel
from domain.repositories.product_repository_abstract import ProductRepositoryAbstract

class ProductRepository(ProductRepositoryAbstract):

    def get_all(self):
        products = ProductModel.get_all_active_products()
        return products

    def get_by_id(self, id):
        product = ProductModel.find_product(id)
        if not product:
            return None
        return product

    def create(self, data):
        product = ProductModel(**data)
        product.save_product()
        return product

    def update(self, id, data):
        product = ProductModel.find_product(id)
        if not product:
            return None
        product.update_product(**data)
        return product

    def delete(self, id):
        product = ProductModel.find_product(id)
        if not product:
            return None
        product.delete_product()
        return product
