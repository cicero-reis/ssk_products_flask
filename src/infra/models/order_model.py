from typing import Any
from datetime import datetime, timezone

from sqlalchemy import event  # type: ignore

from extensions import db


class OrderModel(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)

    def __init__(self, product_id: Any, name: Any, price: Any, quantity: Any) -> Any:
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def json(self) -> Any:
        return {
            "id": self.id,
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
        }

    @classmethod
    def get_all_active_orders(cls: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None)).all()

    @classmethod
    def find_order(cls: Any, id: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None), cls.id == id).first()

    @classmethod
    def find_by_name(cls: Any, name: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None), cls.name == name).first()

    def save_order(self) -> Any:
        db.session.add(self)
        db.session.commit()

    def update_order(self, **kwargs: Any) -> Any:
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        db.session.commit()

    def delete_order(self) -> Any:
        self.deleted_at = datetime.now(timezone.utc)
        db.session.commit()


@event.listens_for(OrderModel, "before_insert")
def before_insert(mapper: Any, connection: Any, target: Any) -> Any:
    target.created_at = datetime.now(timezone.utc)
    target.updated_at = datetime.now(timezone.utc)


@event.listens_for(OrderModel, "before_update")
def before_update(mapper: Any, connection: Any, target: Any) -> Any:
    target.updated_at = datetime.now(timezone.utc)
