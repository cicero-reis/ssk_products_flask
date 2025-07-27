from abc import ABC, abstractmethod
from typing import Any


class UpdateCategoryCommandAbstract(ABC):
    @abstractmethod
    def handle(self, category_id: int, category_data) -> Any:
        pass
