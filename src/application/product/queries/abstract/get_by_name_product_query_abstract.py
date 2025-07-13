from abc import ABC, abstractmethod

class GetByNameProductQueryAbstract(ABC):
    @abstractmethod
    def handle(self, name):
        pass