from typing import Any
from abc import ABC, abstractmethod


class DeleteProductRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, id: Any) -> Any:
        pass
