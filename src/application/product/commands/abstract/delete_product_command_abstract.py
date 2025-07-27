from abc import ABC, abstractmethod
from typing import Any


class DeleteProductCommandAbstract(ABC):
    @abstractmethod
    def handle(self, id: Any) -> Any:
        pass
