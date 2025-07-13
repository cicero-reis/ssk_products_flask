from abc import ABC, abstractmethod


class CreateProductCommandAbstract(ABC):
    @abstractmethod
    def handle(self, data):
        pass
