from abc import ABC, abstractmethod

class UpdateCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def update(self, id, data):
        pass