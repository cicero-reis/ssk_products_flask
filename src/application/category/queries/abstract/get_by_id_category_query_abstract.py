from abc import ABC, abstractmethod

class GetByIdCategoryQueryAbstract(ABC):
    @abstractmethod
    def handle(self, id):
        pass