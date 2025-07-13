from abc import ABC, abstractmethod


class UpdateProductRepositoryAbstract(ABC):
    @abstractmethod
    def update(self, id, data):
        pass
