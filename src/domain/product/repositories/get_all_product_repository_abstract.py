from abc import ABC, abstractmethod
from typing import Any


class GetAllProductRepositoryAbstract(ABC):
    @abstractmethod
    def get_all(self) -> Any:
        pass
