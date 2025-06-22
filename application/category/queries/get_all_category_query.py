from application.category.queries.abstract.get_all_category_query_abstract import GetAllCategoryQueryAbstract
from application.category.dtos.category_dto import CategoryDto

class GetAllCategoryQuery(GetAllCategoryQueryAbstract):

    def __init__(self, repo: GetAllCategoryQueryAbstract):
        self.repo = repo

    def handle(self):
        categories = self.repo.get_all_categories()
        dtos = [CategoryDto.from_entity(category).to_dict() for category in categories]
        return dtos, None
