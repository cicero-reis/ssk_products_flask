from abc import ABC, abstractmethod
from typing import Any


class DeleteCategoryCommandAbstract(ABC):
    @abstractmethod
    def handle(self, id: Any) -> Any:
        pass
