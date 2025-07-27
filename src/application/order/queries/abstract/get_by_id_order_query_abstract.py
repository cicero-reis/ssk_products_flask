from typing import Any
from abc import ABC, abstractmethod

class GetByIdOrderQueryAbstract(ABC):
    @abstractmethod
    def handle(self, order_id: Any) -> Any:
        pass
