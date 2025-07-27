from typing import Any
from abc import ABC, abstractmethod


class GetByNameCategoryQueryAbstract(ABC):
    @abstractmethod
    def handle(self, name: Any) -> Any:
        pass
