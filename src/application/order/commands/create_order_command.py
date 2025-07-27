from typing import Any
from src.application.order.dtos.order_dto import OrderDTO

class CreateOrderCommand:
    def __init__(self, repo: Any, event: Any) -> Any:
        self.repo = repo
        self.event = event

    def handle(self, data: Any) -> Any:
        order = self.repo.create(data)
        self.event.publish_event("order_created", {"order_id": order.id})
        dto = OrderDTO.from_entity(order)
        return dto.to_dict(), None
