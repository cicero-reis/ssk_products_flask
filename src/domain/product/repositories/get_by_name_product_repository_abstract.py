from abc import ABC, abstractmethod
from typing import Any


class GetByNameProductRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_name(self, name: Any) -> Any:
        pass
