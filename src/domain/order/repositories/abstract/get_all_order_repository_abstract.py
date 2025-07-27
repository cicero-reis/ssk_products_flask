from abc import ABC, abstractmethod
from typing import Any


class GetAllOrderRepositoryAbstract(ABC):
    @abstractmethod
    def get_all(self) -> Any:
        pass
