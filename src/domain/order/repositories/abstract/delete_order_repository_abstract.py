from abc import ABC, abstractmethod
from typing import Any


class DeleteOrderRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, order_id: Any) -> Any:
        pass
