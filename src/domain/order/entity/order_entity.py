from typing import Any
class OrderEntity:
    def __init__(
        self,
        id: int,
        product_id: int,
        name: str,
        price: float,
        quantity: int,
    ):
        self.id = id
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
