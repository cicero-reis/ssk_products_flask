from src.application.product.commands.abstract.delete_product_command_abstract import (
    DeleteProductCommandAbstract,
)
from src.application.product.events.abstract.event_product_publisher_abstract import (
    EventProductPublisherAbstract,
)
from src.domain.product.repositories.delete_product_repository_abstract import (
    DeleteProductRepositoryAbstract,
)


class DeleteProductCommand(DeleteProductCommandAbstract):
    def __init__(self, repo: DeleteProductRepositoryAbstract, event: EventProductPublisherAbstract):
        self.repo = repo
        self.event = event

    def handle(self, id):
        product = self.repo.delete(id)
        if not product:
            return None, f"Product id {id} not found"
        self.event.publish_event("product_deleted", {"product_id": id})
        return True, None
