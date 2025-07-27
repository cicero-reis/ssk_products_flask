from typing import Any
from abc import ABC, abstractmethod


class GetAllCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def get_all_categories(self) -> Any:
        pass
