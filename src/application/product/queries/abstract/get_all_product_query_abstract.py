from typing import Any
from abc import ABC, abstractmethod


class GetAllProductQueryAbstract(ABC):
    @abstractmethod
    def handle(self) -> Any:
        pass
