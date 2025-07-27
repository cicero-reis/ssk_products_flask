from typing import Any
from abc import ABC, abstractmethod


class DeleteCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, id: Any) -> Any:
        pass
