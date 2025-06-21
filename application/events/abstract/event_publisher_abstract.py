from abc import ABC, abstractmethod

class EventPublisherAbstract(ABC):

    @abstractmethod
    def publish_event(self, event_name: str, data: dict):
        pass
