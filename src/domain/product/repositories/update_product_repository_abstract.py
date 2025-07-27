from typing import Any
from abc import ABC, abstractmethod


class UpdateProductRepositoryAbstract(ABC):
    @abstractmethod
    def update(self, id: Any, data: Any) -> Any:
        pass
