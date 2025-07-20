from abc import ABC, abstractmethod


class EventProductRepositoryAbstract(ABC):
    @abstractmethod
    def save_event(self, event_type, data):
        pass

    @abstractmethod
    def get_events(self, product_id):
        pass
