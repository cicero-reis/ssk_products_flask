from abc import ABC, abstractmethod
from typing import Any


class DeleteProductRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, id: Any) -> Any:
        pass
