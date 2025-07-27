from typing import Any


from src.infra.order.repositories.mongo_order_repository import MongoOrderRepository
from flask import current_app


class DeleteOrderRepository:
    def __init__(self, event_repo: Any = None) -> Any:
        self.event_repo = event_repo

    @property
    def mongo_repo(self) -> Any:
        db = current_app.extensions.get('mongo_db')
        if db is None:
            raise RuntimeError('MongoDB não inicializado. Chame init_app(app) antes de usar os repositórios.')
        return MongoOrderRepository(db)

    def delete(self, order_id: Any) -> Any:
        deleted = self.mongo_repo.delete(order_id)
        if self.event_repo and deleted:
            self.event_repo.save_event("order_deleted", {"order_id": order_id})
        return deleted
