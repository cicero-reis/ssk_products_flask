from typing import Any
from abc import ABC, abstractmethod


class GetByIdProductRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_id(self, id: Any) -> Any:
        pass
