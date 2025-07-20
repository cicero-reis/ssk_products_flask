from src.application.category.commands.abstract.delete_category_command_abstract import (
    DeleteCategoryCommandAbstract,
)
from src.application.category.events.abstract.event_category_publisher_abstract import (
    EventCategoryPublisherAbstract,
)
from src.domain.category.repositories.delete_category_repository_abstract import (
    DeleteCategoryRepositoryAbstract,
)


class DeleteCategoryCommand(DeleteCategoryCommandAbstract):
    def __init__(self, repo: DeleteCategoryRepositoryAbstract, event: EventCategoryPublisherAbstract):
        self.repo = repo
        self.event = event

    def handle(self, id):
        category = self.repo.delete(id)

        if not category:
            return None, f"Category id {id} not found"

        self.event.publish_event("category_deleted", {"category_id": id})

        return True, None
