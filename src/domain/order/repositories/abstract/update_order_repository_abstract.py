from typing import Any
from abc import ABC, abstractmethod

class UpdateOrderRepositoryAbstract(ABC):
    @abstractmethod
    def update(self, order_id: Any, data: Any) -> Any:
        pass
