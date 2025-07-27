from typing import Any
from src.application.product.commands.abstract.create_product_command_abstract import (
    CreateProductCommandAbstract,
)
from src.application.product.dtos.product_dto import ProductDTO
from src.application.product.events.abstract.event_product_publisher_abstract import (
    EventProductPublisherAbstract,
)
from src.domain.product.repositories.create_product_repository_abstract import (
    CreateProductRepositoryAbstract,
)

class CreateProductCommand(CreateProductCommandAbstract):
    def __init__(self, repo: CreateProductRepositoryAbstract, event: EventProductPublisherAbstract) -> Any:
        self.repo = repo
        self.event = event

    def handle(self, data: Any) -> Any:
        product = self.repo.create(data)

        self.event.publish_event("product_created", {"product_id": product.id})

        dto = ProductDTO.from_entity(product)

        return dto.to_dict(), None
