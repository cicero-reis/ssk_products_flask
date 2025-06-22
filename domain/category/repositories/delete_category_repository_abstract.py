from abc import ABC, abstractmethod

class DeleteCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass
