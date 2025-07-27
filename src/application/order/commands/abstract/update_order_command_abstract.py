from typing import Any
from abc import ABC, abstractmethod

class UpdateOrderCommandAbstract(ABC):
    @abstractmethod
    def handle(self, order_id: Any, data: Any) -> Any:
        pass
