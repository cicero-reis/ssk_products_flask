from abc import ABC, abstractmethod
from typing import Any


class UpdateProductRepositoryAbstract(ABC):
    @abstractmethod
    def update(self, id: Any, data: Any) -> Any:
        pass
