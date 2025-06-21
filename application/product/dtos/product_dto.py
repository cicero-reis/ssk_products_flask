class ProductDTO:
    def __init__(self, id, name, description, price, category_id, image):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.image = image

    @staticmethod
    def from_entity(product):
        return ProductDTO(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id,
            image=product.image
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category_id": self.category_id,
            "image": self.image
        }
