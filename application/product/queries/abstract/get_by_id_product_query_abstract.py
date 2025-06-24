from abc import ABC, abstractmethod

class GetByIdProductQueryAbstract(ABC):
    @abstractmethod
    def handle(self, id):
        pass