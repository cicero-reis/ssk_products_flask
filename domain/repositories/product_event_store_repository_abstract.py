from abc import ABC, abstractmethod

class ProductEventStoreRepositoryAbstract(ABC):
    @abstractmethod
    def save_event(self, aggregate_id, event_type, data):
        pass
    @abstractmethod
    def get_events_for_aggregate(self, aggregate_id):
        pass
