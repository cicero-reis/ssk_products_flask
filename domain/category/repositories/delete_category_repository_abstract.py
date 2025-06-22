from abc import ABC, abstractmethod

class DeleteCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, id):
        pass
