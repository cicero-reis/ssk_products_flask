class ProductEntitie:
    def __init__(self, id: int, name: str, description: str, price: float, category: int, image: str):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image = image