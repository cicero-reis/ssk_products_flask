from domain.category.repositories.get_by_name_category_repository_abstract import GetByNameCategoryRepositoryAbstract
from infra.models.category_model import CategoryModel

class GetByNameCategoryRepository(GetByNameCategoryRepositoryAbstract):

    def get_by_name(self, name):
        category = CategoryModel.find_by_name(name)
        if not category:
            return None
        return category
