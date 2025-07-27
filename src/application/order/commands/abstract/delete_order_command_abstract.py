from abc import ABC, abstractmethod
from typing import Any


class DeleteOrderCommandAbstract(ABC):
    @abstractmethod
    def handle(self, order_id: Any) -> Any:
        pass
