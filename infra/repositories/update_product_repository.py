from infra.models.product_model import ProductModel
from domain.repositories.update_product_repository_abstract import UpdateProductRepositoryAbstract
from domain.repositories.product_event_store_repository_abstract import ProductEventStoreRepositoryAbstract

class UpdateProductRepository(UpdateProductRepositoryAbstract):

    def __init__(self, event_store_repo: ProductEventStoreRepositoryAbstract):
        self.event_store_repo = event_store_repo
    
    def update(self, id, data):
        product = ProductModel.find_product(id)
        if not product:
            return None
        product.update_product(**data)

        event = self.event_store_repo.save_event(
            "ProductUpdated",
            product
        )

        return product
