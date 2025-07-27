from typing import Any
from abc import ABC, abstractmethod


class CreateCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def create(self, data: Any) -> Any:
        pass
