from abc import ABC, abstractmethod

class DeleteCategoryCommandAbstract(ABC):
    @abstractmethod
    def handle(self, id):
        pass