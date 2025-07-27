from typing import Any
from abc import ABC, abstractmethod

class DeleteOrderRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, order_id: Any) -> Any:
        pass
