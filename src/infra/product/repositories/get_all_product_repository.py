from src.domain.product.repositories.get_all_product_repository_abstract import (
    GetAllProductRepositoryAbstract,
)
from src.infra.models.product_model import ProductModel


class GetAllProductRepository(GetAllProductRepositoryAbstract):
    def get_all(self):
        products = ProductModel.get_all_active_products()
        return products
