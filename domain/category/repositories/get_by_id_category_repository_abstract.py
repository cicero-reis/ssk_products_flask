from abc import ABC, abstractmethod

class GetByIdCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def get_by_id(self, id: str) -> dict:
        pass