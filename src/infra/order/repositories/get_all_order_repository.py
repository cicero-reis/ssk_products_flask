from typing import Any

from src.infra.order.repositories.mongo_order_repository import MongoOrderRepository
from flask import current_app


class GetAllOrderRepository:
    def __init__(self) -> Any:
        pass


    @property
    def mongo_repo(self) -> Any:
        db = current_app.extensions.get('mongo_db')
        if db is None:
            raise RuntimeError('MongoDB não inicializado. Chame init_app(app) antes de usar os repositórios.')
        return MongoOrderRepository(db)

    def get_all(self) -> Any:
        return [order.to_dict() for order in self.mongo_repo.get_all()]
