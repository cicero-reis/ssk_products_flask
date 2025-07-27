from typing import Any
from abc import ABC, abstractmethod

class CreateOrderRepositoryAbstract(ABC):
    @abstractmethod
    def create(self, data: Any) -> Any:
        pass
