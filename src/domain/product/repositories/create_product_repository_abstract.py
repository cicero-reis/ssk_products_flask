from abc import ABC, abstractmethod


class CreateProductRepositoryAbstract(ABC):
    @abstractmethod
    def create(self, data):
        pass
