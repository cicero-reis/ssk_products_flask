from typing import Any
class OrderDTO:
    def __init__(self, id: Any, product_id: Any, name: Any, price: Any, quantity: Any) -> Any:
        self.id = id
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def from_entity(order: Any) -> Any:
        return OrderDTO(
            id=order.id,
            product_id=order.product_id,
            name=order.name,
            price=order.price,
            quantity=order.quantity,
        )

    def to_dict(self) -> Any:
        return {
            "id": self.id,
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
        }
