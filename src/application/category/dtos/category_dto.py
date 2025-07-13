class CategoryDto:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    @staticmethod
    def from_entity(category):
        return CategoryDto(id=category.id, name=category.name, description=category.description)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}
