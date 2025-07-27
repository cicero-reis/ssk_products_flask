from typing import Any

from flask import current_app

from src.infra.order.repositories.mongo_order_repository import MongoOrderRepository


class GetByIdOrderRepository:
    def __init__(self) -> Any:
        pass

    @property
    def mongo_repo(self) -> Any:
        db = current_app.extensions.get('mongo_db')
        if db is None:
            raise RuntimeError('MongoDB não inicializado. Chame init_app(app) antes de usar os repositórios.')
        return MongoOrderRepository(db)

    def get_by_id(self, order_id: Any) -> Any:
        order = self.mongo_repo.get_by_id(order_id)
        return order.to_dict() if order else None
