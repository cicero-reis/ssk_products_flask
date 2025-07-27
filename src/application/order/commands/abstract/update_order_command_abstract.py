from abc import ABC, abstractmethod
from typing import Any


class UpdateOrderCommandAbstract(ABC):
    @abstractmethod
    def handle(self, order_id: Any, data: Any) -> Any:
        pass
