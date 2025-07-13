from abc import ABC, abstractmethod


class DeleteProductRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, id):
        pass
