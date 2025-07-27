from abc import ABC, abstractmethod
from typing import Any


class UpdateProductCommandAbstract(ABC):
    @abstractmethod
    def handle(self, id: Any, data: Any) -> Any:
        pass
