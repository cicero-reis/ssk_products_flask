from typing import Any

from flask import current_app

from src.infra.order.repositories.mongo_order_repository import MongoOrderRepository


class UpdateOrderRepository:
    def __init__(self, event_repo: Any = None) -> Any:
        self.event_repo = event_repo

    @property
    def mongo_repo(self) -> Any:
        db = current_app.extensions.get('mongo_db')
        if db is None:
            raise RuntimeError('MongoDB não inicializado. Chame init_app(app) antes de usar os repositórios.')
        return MongoOrderRepository(db)

    def update(self, order_id: Any, data: Any) -> Any:
        order = self.mongo_repo.update(order_id, data)
        if self.event_repo and order:
            self.event_repo.save_event("order_updated", order)
        return order.to_dict() if order else None
