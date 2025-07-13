from src.infra.models.category_model import CategoryModel
from src.domain.category.repositories.get_all_category_repository_abstract import GetAllCategoryRepositoryAbstract

class GetAllCategoryRepository(GetAllCategoryRepositoryAbstract):

    def get_all_categories(self):
        return CategoryModel.get_all_active_categories()
        
