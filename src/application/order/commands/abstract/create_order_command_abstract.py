from abc import ABC, abstractmethod
from typing import Any


class CreateOrderCommandAbstract(ABC):
    @abstractmethod
    def handle(self, data: Any) -> Any:
        pass
