from abc import ABC, abstractmethod
from typing import Any


class GetAllOrderQueryAbstract(ABC):
    @abstractmethod
    def handle(self) -> Any:
        pass
