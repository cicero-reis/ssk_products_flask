from abc import ABC, abstractmethod
from typing import Any


class GetAllCategoryQueryAbstract(ABC):
    @abstractmethod
    def handle(self) -> Any:
        pass
