from abc import ABC, abstractmethod
from typing import Any


class GetByIdOrderRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_id(self, order_id: Any) -> Any:
        pass
