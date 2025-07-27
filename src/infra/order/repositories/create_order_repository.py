
from typing import Any

from flask import current_app

from src.infra.order.repositories.mongo_order_repository import MongoOrderRepository


class CreateOrderRepository:
    def __init__(self, event_repo: Any = None) -> Any:
        self.event_repo = event_repo

    @property
    def mongo_repo(self) -> Any:
        db = current_app.extensions.get('mongo_db')
        if db is None:
            raise RuntimeError('MongoDB não inicializado. Chame init_app(app) antes de usar os repositórios.')
        return MongoOrderRepository(db)

    def create(self, data: Any) -> Any:
        return self.mongo_repo.create(data)
