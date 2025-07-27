from typing import Any
from abc import ABC, abstractmethod

class CreateOrderCommandAbstract(ABC):
    @abstractmethod
    def handle(self, data: Any) -> Any:
        pass
