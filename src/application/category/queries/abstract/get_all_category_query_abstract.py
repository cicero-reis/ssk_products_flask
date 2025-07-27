from typing import Any
from abc import ABC, abstractmethod


class GetAllCategoryQueryAbstract(ABC):
    @abstractmethod
    def handle(self) -> Any:
        pass
