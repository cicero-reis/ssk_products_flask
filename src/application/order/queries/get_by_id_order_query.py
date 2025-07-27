from typing import Any
from src.application.order.dtos.order_dto import OrderDTO

class GetByIdOrderQuery:
    def __init__(self, repo: Any) -> Any:
        self.repo = repo

    def handle(self, order_id: Any) -> Any:
        order = self.repo.get_by_id(order_id)
        if order:
            return OrderDTO.from_entity(order).to_dict(), None
        return None, "Order not found"
