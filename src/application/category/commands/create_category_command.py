from src.application.category.commands.abstract.create_category_command_abstract import (
    CreateCategoryCommandAbstract,
)
from src.application.category.dtos.category_dto import CategoryDto
from src.application.category.events.abstract.event_category_publisher_abstract import (
    EventCategoryPublisherAbstract,
)
from src.domain.category.repositories.create_category_repository_abstract import (
    CreateCategoryRepositoryAbstract,
)


class CreateCategoryCommand(CreateCategoryCommandAbstract):
    def __init__(
        self, repo: CreateCategoryRepositoryAbstract, event: EventCategoryPublisherAbstract
    ):
        self.repo = repo
        self.event = event

    def handle(self, data):
        category = self.repo.create(data)

        self.event.publish_event("category_created", {"category_id": category.id})

        dto = CategoryDto.from_entity(category)

        return dto.to_dict(), None
