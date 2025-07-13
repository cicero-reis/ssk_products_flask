from src.domain.category.repositories.get_by_id_category_repository_abstract import GetByIdCategoryRepositoryAbstract
from src.infra.models.category_model import CategoryModel

class GetByIdCategoryRepository(GetByIdCategoryRepositoryAbstract):

    def get_by_id(self, id):
        category = CategoryModel.find_by_id(id)
        if not category:
            return None
        return category
