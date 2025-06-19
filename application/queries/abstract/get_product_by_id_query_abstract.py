from abc import ABC, abstractmethod

class GetProductByIdQueryAbstract(ABC):
    @abstractmethod
    def handle(self, id):
        pass