from abc import ABC, abstractmethod
from typing import Any


class UpdateCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def update(self, id: Any, data: Any) -> Any:
        pass
