from typing import Any
from abc import ABC, abstractmethod


class EventProductRepositoryAbstract(ABC):
    @abstractmethod
    def save_event(self, event_type: Any, data: Any) -> Any:
        pass

    @abstractmethod
    def get_events(self, product_id: Any) -> Any:
        pass
