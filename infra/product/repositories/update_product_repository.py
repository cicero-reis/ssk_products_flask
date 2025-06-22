from infra.models.product_model import ProductModel
from domain.product.repositories.update_product_repository_abstract import UpdateProductRepositoryAbstract
from domain.product.repositories.event_product_repository_abstract import EventProductRepositoryAbstract

class UpdateProductRepository(UpdateProductRepositoryAbstract):

    def __init__(self, event_repo: EventProductRepositoryAbstract):
        self.event_repo = event_repo
    
    def update(self, id, data):
        product = ProductModel.find_product(id)
        if not product:
            return None
        product.update_product(**data)

        event = self.event_repo.save_event(
            "ProductUpdated",
            product
        )

        return product
