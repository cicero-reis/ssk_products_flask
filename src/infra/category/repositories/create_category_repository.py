from typing import Any
from src.domain.category.repositories.create_category_repository_abstract import (
    CreateCategoryRepositoryAbstract,
)
from src.domain.category.repositories.event_category_repository_abstract import (
    EventCategoryRepositoryAbstract,
)
from src.infra.models.category_model import CategoryModel


class CreateCategoryRepository(CreateCategoryRepositoryAbstract):
    def __init__(self, event: EventCategoryRepositoryAbstract) -> Any:
        self.event = event

    def create(self, data: Any) -> Any:
        category = CategoryModel(**data)
        category.save_category()

        self.event.save_event("category_created", category)

        return category
