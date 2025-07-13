from src.application.category.queries.abstract.get_by_name_category_query_abstract import GetByNameCategoryQueryAbstract
from src.domain.category.repositories.get_by_name_category_repository_abstract import GetByNameCategoryRepositoryAbstract
from src.application.category.dtos.category_dto import CategoryDto

class GetByNameCategoryQuery(GetByNameCategoryQueryAbstract):
    def __init__(self, repo: GetByNameCategoryRepositoryAbstract):
        self.repo = repo

    def handle(self, name):
        category = self.repo.get_by_name(name)

        if not category:
            return None, f'Category name {name} not found'

        dto = CategoryDto.from_entity(category)
        
        return dto.to_dict(), None