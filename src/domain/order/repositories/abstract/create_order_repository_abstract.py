from abc import ABC, abstractmethod
from typing import Any


class CreateOrderRepositoryAbstract(ABC):
    @abstractmethod
    def create(self, data: Any) -> Any:
        pass
