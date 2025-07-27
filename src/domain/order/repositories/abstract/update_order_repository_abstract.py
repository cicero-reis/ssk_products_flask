from abc import ABC, abstractmethod
from typing import Any


class UpdateOrderRepositoryAbstract(ABC):
    @abstractmethod
    def update(self, order_id: Any, data: Any) -> Any:
        pass
