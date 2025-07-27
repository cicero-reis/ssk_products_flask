from abc import ABC, abstractmethod
from typing import Any


class GetAllProductQueryAbstract(ABC):
    @abstractmethod
    def handle(self) -> Any:
        pass
