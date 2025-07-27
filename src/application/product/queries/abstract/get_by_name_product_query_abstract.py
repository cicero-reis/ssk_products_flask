from typing import Any
from abc import ABC, abstractmethod


class GetByNameProductQueryAbstract(ABC):
    @abstractmethod
    def handle(self, name: Any) -> Any:
        pass
