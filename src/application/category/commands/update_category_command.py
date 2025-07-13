from src.application.category.commands.abstract.update_category_command_abstract import (
    UpdateCategoryCommandAbstract,
)
from src.application.category.dtos.category_dto import CategoryDto
from src.application.category.events.abstract.event_category_publisher_abstract import (
    EventCategoryPublisherAbstract,
)
from src.domain.category.repositories.update_category_repository_abstract import (
    UpdateCategoryRepositoryAbstract,
)


class UpdateCategoryCommand(UpdateCategoryCommandAbstract):
    def __init__(
        self, repo: UpdateCategoryRepositoryAbstract, event: EventCategoryPublisherAbstract
    ):
        self.repo = repo
        self.event = event

    def handle(self, id, data):
        success, category = self.repo.update(id, data)

        if not success:
            return None, f"Category id {id} not found"

        self.event.publish_event("category_updated", {"category_id": category.id})

        dto = CategoryDto.from_entity(category)

        return dto.to_dict(), None
