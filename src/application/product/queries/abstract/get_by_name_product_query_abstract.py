from abc import ABC, abstractmethod
from typing import Any


class GetByNameProductQueryAbstract(ABC):
    @abstractmethod
    def handle(self, name: Any) -> Any:
        pass
