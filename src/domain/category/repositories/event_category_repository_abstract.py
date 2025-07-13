from abc import ABC, abstractmethod

class EventCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def save_event(self, category_id, event_type, data):
        pass

    @abstractmethod
    def get_events(self, category_id):
        pass