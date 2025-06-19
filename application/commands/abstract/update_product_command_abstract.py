from abc import ABC, abstractmethod

class UpdateProductCommandAbstract(ABC):
    @abstractmethod
    def handle(self, id, data):
        pass