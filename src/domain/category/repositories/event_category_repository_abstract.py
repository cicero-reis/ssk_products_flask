from abc import ABC, abstractmethod
from typing import Any


class EventCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def save_event(self, event_type: Any, data: Any) -> Any:
        pass

    @abstractmethod
    def get_events(self, category_id: Any) -> Any:
        pass
