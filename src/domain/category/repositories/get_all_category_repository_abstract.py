from abc import ABC, abstractmethod
from typing import Any


class GetAllCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def get_all_categories(self) -> Any:
        pass
