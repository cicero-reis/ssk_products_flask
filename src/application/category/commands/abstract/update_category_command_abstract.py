from abc import ABC, abstractmethod


class UpdateCategoryCommandAbstract(ABC):
    @abstractmethod
    def handle(self, category_id: int, category_data):
        pass
