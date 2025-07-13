from abc import ABC, abstractmethod


class CreateCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def create(self, data):
        pass
