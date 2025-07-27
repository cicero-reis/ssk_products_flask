from typing import Any
class DeleteOrderCommand:
    def __init__(self, repo: Any, event: Any) -> Any:
        self.repo = repo
        self.event = event

    def handle(self, order_id: Any) -> Any:
        self.repo.delete(order_id)
        self.event.publish_event("order_deleted", {"order_id": order_id})
        return {"deleted": True}, None
