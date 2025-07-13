from abc import ABC, abstractmethod

class GetByNameProductRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_name(self, name):
        pass