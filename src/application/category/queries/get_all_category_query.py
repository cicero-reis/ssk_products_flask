from src.application.category.dtos.category_dto import CategoryDto
from src.application.category.queries.abstract.get_all_category_query_abstract import (
    GetAllCategoryQueryAbstract,
)


class GetAllCategoryQuery(GetAllCategoryQueryAbstract):
    def __init__(self, repo: GetAllCategoryQueryAbstract):
        self.repo = repo

    def handle(self):
        categories = self.repo.get_all_categories()
        dtos = [CategoryDto.from_entity(category).to_dict() for category in categories]
        return dtos, None
