from abc import ABC, abstractmethod


class GetAllProductQueryAbstract(ABC):
    @abstractmethod
    def handle(self):
        pass
