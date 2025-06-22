from abc import ABC, abstractmethod 

class GetAllCategoryQueryAbstract(ABC):
    @abstractmethod
    def handle(self):
        pass