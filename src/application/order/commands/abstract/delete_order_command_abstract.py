from typing import Any
from abc import ABC, abstractmethod

class DeleteOrderCommandAbstract(ABC):
    @abstractmethod
    def handle(self, order_id: Any) -> Any:
        pass
