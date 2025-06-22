from infra.models.category_model import CategoryModel
from domain.category.repositories.update_category_repository_abstract import UpdateCategoryRepositoryAbstract
from domain.category.repositories.event_category_repository_abstract import EventCategoryRepositoryAbstract

class UpdateCategoryRepository(UpdateCategoryRepositoryAbstract):
    def __init__(self, event_repo: EventCategoryRepositoryAbstract):
        self.event_repo = event_repo

    def update(self, id, data):
        category = CategoryModel.find_by_id(id)

        if not category:
            return False, f'Category id {id} not found'

        category.update(**data)

        self.event_repo.save_event(
            'CategoryUpdated',
            category
        )

        return category
