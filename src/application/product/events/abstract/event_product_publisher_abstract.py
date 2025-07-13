from abc import ABC, abstractmethod

class EventProductPublisherAbstract(ABC):

    @abstractmethod
    def publish_event(self, event_name: str, data: dict):
        pass
