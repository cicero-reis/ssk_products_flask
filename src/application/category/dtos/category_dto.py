from typing import Any


class CategoryDto:
    def __init__(self, id: Any, name: Any, description: Any) -> Any:
        self.id = id
        self.name = name
        self.description = description

    @staticmethod
    def from_entity(category: Any) -> Any:
        return CategoryDto(id=category.id, name=category.name, description=category.description)

    def to_dict(self) -> Any:
        return {"id": self.id, "name": self.name, "description": self.description}
