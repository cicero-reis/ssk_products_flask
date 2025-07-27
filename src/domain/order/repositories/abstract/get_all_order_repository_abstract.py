from typing import Any
from abc import ABC, abstractmethod

class GetAllOrderRepositoryAbstract(ABC):
    @abstractmethod
    def get_all(self) -> Any:
        pass
