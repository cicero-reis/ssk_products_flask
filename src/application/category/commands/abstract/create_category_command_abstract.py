from typing import Any
from abc import ABC, abstractmethod


class CreateCategoryCommandAbstract(ABC):
    @abstractmethod
    def handle(self, data: Any) -> Any:
        pass
