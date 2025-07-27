from typing import Any
from src.application.order.dtos.order_dto import OrderDTO

class UpdateOrderCommand:
    def __init__(self, repo: Any, event: Any) -> Any:
        self.repo = repo
        self.event = event

    def handle(self, order_id: Any, data: Any) -> Any:
        order = self.repo.update(order_id, data)
        self.event.publish_event("order_updated", {"order_id": order.id})
        dto = OrderDTO.from_entity(order)
        return dto.to_dict(), None
