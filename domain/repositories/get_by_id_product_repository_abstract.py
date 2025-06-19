from abc import ABC, abstractmethod

class GetByIdProductRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_id(self, id):
        pass