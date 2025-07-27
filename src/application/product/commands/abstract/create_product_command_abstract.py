from typing import Any
from abc import ABC, abstractmethod


class CreateProductCommandAbstract(ABC):
    @abstractmethod
    def handle(self, data: Any) -> Any:
        pass
