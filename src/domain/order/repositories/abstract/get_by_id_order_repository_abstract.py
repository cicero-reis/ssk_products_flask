from typing import Any
from abc import ABC, abstractmethod

class GetByIdOrderRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_id(self, order_id: Any) -> Any:
        pass
