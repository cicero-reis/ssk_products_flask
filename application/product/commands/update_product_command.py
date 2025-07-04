from domain.product.repositories.update_product_repository_abstract import UpdateProductRepositoryAbstract
from application.product.commands.abstract.update_product_command_abstract import UpdateProductCommandAbstract
from application.category.events.abstract.event_category_publisher_abstract import EventCategoryPublisherAbstract
from application.product.dtos.product_dto import ProductDTO

class UpdateProductCommand(UpdateProductCommandAbstract):
    def __init__(self, repo: UpdateProductRepositoryAbstract, event: EventCategoryPublisherAbstract):
        self.repo = repo
        self.event = event

    def handle(self, id, data):

        success, product = self.repo.update(id, data)

        if not success:
            return None, f'Product id {id} not found'

        self.event.publish_event("product_updated", {"product_id": product.id})

        dto = ProductDTO.from_entity(product)

        return dto.to_dict(), None

        