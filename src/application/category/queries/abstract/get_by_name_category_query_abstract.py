from abc import ABC, abstractmethod


class GetByNameCategoryQueryAbstract(ABC):
    @abstractmethod
    def handle(self, name):
        pass
