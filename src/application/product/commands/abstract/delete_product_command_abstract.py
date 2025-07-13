from abc import ABC, abstractmethod


class DeleteProductCommandAbstract(ABC):
    @abstractmethod
    def handle(self, id):
        pass
