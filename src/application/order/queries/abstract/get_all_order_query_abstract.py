from typing import Any
from abc import ABC, abstractmethod

class GetAllOrderQueryAbstract(ABC):
    @abstractmethod
    def handle(self) -> Any:
        pass
