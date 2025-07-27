from typing import Any
from src.application.order.dtos.order_dto import OrderDTO

class GetAllOrderQuery:
    def __init__(self, repo: Any) -> Any:
        self.repo = repo

    def handle(self) -> Any:
        orders = self.repo.get_all()
        dtos = [OrderDTO.from_entity(o).to_dict() for o in orders]
        return dtos, None
