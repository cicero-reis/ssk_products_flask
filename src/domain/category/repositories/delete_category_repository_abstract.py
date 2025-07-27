from abc import ABC, abstractmethod
from typing import Any


class DeleteCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, id: Any) -> Any:
        pass
