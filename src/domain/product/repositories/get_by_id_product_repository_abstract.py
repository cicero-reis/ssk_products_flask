from abc import ABC, abstractmethod
from typing import Any


class GetByIdProductRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_id(self, id: Any) -> Any:
        pass
