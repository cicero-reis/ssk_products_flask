from src.application.category.dtos.category_dto import CategoryDto
from src.application.category.queries.abstract.get_by_id_category_query_abstract import (
    GetByIdCategoryQueryAbstract,
)
from src.domain.category.repositories.get_by_id_category_repository_abstract import (
    GetByIdCategoryRepositoryAbstract,
)


class GetByIdCategoryQuery(GetByIdCategoryQueryAbstract):
    def __init__(self, repo: GetByIdCategoryRepositoryAbstract):
        self.repo = repo

    def handle(self, id):
        category = self.repo.get_by_id(id)

        if not category:
            return None, f"Category id {id} not found"

        dto = CategoryDto.from_entity(category)

        return dto.to_dict(), None
