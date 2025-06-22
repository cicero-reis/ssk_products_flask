from abc import ABC, abstractmethod

class UpdateCategoryCommandAbstract(ABC):
    @abstractmethod
    def update(self, category_id: int, data):
        pass