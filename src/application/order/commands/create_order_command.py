from typing import Any

from src.application.order.dtos.order_dto import OrderDTO


class CreateOrderCommand:
    def __init__(self, repo: Any, event: Any) -> Any:
        self.repo = repo
        self.event = event

    def handle(self, data: Any) -> Any:
        order = self.repo.create(data)
        assert hasattr(order, 'id'), f"Esperado entidade OrderMongoModel, recebido: {type(order)}"
        dto = OrderDTO.from_entity(order)
        return dto, None
