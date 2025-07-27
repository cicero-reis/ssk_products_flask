from typing import Any
from abc import ABC, abstractmethod


class UpdateProductCommandAbstract(ABC):
    @abstractmethod
    def handle(self, id: Any, data: Any) -> Any:
        pass
