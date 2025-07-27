from typing import Any

from src.domain.category.repositories.get_all_category_repository_abstract import (
    GetAllCategoryRepositoryAbstract,
)
from src.infra.models.category_model import CategoryModel


class GetAllCategoryRepository(GetAllCategoryRepositoryAbstract):
    def get_all_categories(self) -> Any:
        return CategoryModel.get_all_categories()
