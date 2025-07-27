from typing import Any


class OrderDTO:
    def __init__(self, id: Any, products: list, order_number: Any, created_at: Any, updated_at: Any, deleted_at: Any) -> None:
        self.id = id
        self.products = products
        self.order_number = order_number
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    @staticmethod
    def from_entity(order) -> "OrderDTO":
        if isinstance(order, dict):
            return OrderDTO(
                id=str(order.get("_id", "")),
                products=order.get("products", []),
                order_number=order.get("order_number"),
                created_at=order.get("created_at"),
                updated_at=order.get("updated_at"),
                deleted_at=order.get("deleted_at"),
            )
        return OrderDTO(
            id=order.id,
            products=order.products,
            order_number=order.order_number,
            created_at=order.created_at,
            updated_at=order.updated_at,
            deleted_at=order.deleted_at,
        )

    def to_dict(self) -> Any:
        from datetime import datetime
        def iso(dt):
            return dt.isoformat() if isinstance(dt, datetime) else dt
        return {
            "id": self.id,
            "products": self.products,
            "order_number": self.order_number,
            "created_at": iso(self.created_at),
            "updated_at": iso(self.updated_at),
            "deleted_at": iso(self.deleted_at) if self.deleted_at else None,
        }
