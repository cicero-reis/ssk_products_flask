from abc import ABC, abstractmethod
from typing import Any


class GetByNameCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Any:
        pass
