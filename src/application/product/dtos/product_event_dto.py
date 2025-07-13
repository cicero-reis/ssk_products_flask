class ProductEventDTO:
    def __init__(self, id, product_id, action, data, version, timestamp):
        self.id = id
        self.product_id = product_id
        self.action = action
        self.data = data
        self.timestamp = timestamp

    @staticmethod
    def from_entity(event):
        return ProductEventDTO(
            id=event.id,
            product_id=event.product_id,
            action=event.action,
            data=event.data,
            timestamp=event.timestamp,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category_id": self.category_id,
            "image": self.image,
        }
