from src.application.product.commands.abstract.update_product_command_abstract import (
    UpdateProductCommandAbstract,
)
from src.application.product.dtos.product_dto import ProductDTO
from src.application.product.events.abstract.event_product_publisher_abstract import (
    EventProductPublisherAbstract,
)
from src.domain.product.repositories.update_product_repository_abstract import (
    UpdateProductRepositoryAbstract,
)


class UpdateProductCommand(UpdateProductCommandAbstract):
    def __init__(
        self, repo: UpdateProductRepositoryAbstract, event: EventProductPublisherAbstract
    ):
        self.repo = repo
        self.event = event

    def handle(self, id, data):
        success, product = self.repo.update(id, data)

        if not success:
            return None, f"Product id {id} not found"

        self.event.publish_event("product_updated", {"product_id": product.id})

        dto = ProductDTO.from_entity(product)

        return dto.to_dict(), None
