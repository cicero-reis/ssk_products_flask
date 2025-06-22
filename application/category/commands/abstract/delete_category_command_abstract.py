from abc import ABC, abstractmethod

class DeleteCategoryCommandAbstract(ABC)
    @abstractmethod
    def handle(self, category_id: int) -> None:
        pass