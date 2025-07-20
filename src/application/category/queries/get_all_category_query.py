from src.application.category.dtos.category_dto import CategoryDto
from src.application.category.queries.abstract.get_all_category_query_abstract import (
    GetAllCategoryQueryAbstract,
)
from src.domain.category.repositories.get_all_category_repository_abstract import (
    GetAllCategoryRepositoryAbstract,
)


class GetAllCategoryQuery(GetAllCategoryQueryAbstract):
    def __init__(self, repo: GetAllCategoryRepositoryAbstract):
        self.repo = repo

    def handle(self):
        categories = self.repo.get_all_categories()
        print(f"Retrieved {len(categories)} categories from the repository.")
        dtos = [CategoryDto.from_entity(category).to_dict() for category in categories]
        return dtos, None
