from abc import ABC, abstractmethod


class GetAllProductRepositoryAbstract(ABC):
    @abstractmethod
    def get_all(self):
        pass
