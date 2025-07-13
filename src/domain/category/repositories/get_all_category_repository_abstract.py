
from abc import ABC, abstractmethod
 
class GetAllCategoryRepositoryAbstract(ABC):
    @abstractmethod
    def get_all_categories(self):
        pass