from abc import ABC, abstractmethod

class CreateCategoryCommandAbstract(ABC):
    @abstractmethod
    def handle(self, data):
        pass