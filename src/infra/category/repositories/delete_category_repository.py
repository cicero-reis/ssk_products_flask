from src.domain.category.repositories.delete_category_repository_abstract import (
    DeleteCategoryRepositoryAbstract,
)
from src.domain.category.repositories.event_category_repository_abstract import (
    EventCategoryRepositoryAbstract,
)
from src.infra.models.category_model import CategoryModel


class DeleteCategoryRepository(DeleteCategoryRepositoryAbstract):
    def __init__(self, event_repo: EventCategoryRepositoryAbstract):
        self.event_repo = event_repo

    def delete(self, id: int):
        category = CategoryModel.find_by_id(id)

        if not category:
            return None

        category.delete()

        self.event_repo.save_event("CategoryDeleted", category)

        return category
