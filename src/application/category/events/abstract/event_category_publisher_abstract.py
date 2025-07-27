from abc import ABC, abstractmethod
from typing import Any


class EventCategoryPublisherAbstract(ABC):
    @abstractmethod
    def publish_event(self, event_name: str, data: dict) -> Any:
        pass
