from typing import Any
from abc import ABC, abstractmethod


class GetByNameCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> Any:
        pass
