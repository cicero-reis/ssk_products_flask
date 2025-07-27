from datetime import datetime
from typing import Any

from bson import ObjectId


class OrderMongoModel:
    def __init__(self, products: list[dict], order_number: Any = None, _id: Any = None, created_at: Any = None, updated_at: Any = None, deleted_at: Any = None) -> Any:
        self.id = str(_id) if _id else None
        self.products = products
        self.order_number = order_number
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()
        self.deleted_at = deleted_at

    def to_dict(self) -> Any:
        return {
            "_id": ObjectId(self.id) if self.id else None,
            "products": self.products,
            "order_number": self.order_number,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
        }

    @staticmethod
    def from_dict(data: Any) -> Any:
        return OrderMongoModel(
            products=data.get("products", []),
            order_number=data.get("order_number"),
            _id=data.get("_id"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            deleted_at=data.get("deleted_at"),
        )
