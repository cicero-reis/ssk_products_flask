from datetime import datetime, timezone
from typing import Any

from sqlalchemy import event  # type: ignore

from extensions import db


class ProductModel(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)

    # Arquivo no S3
    original_name = db.Column(db.String(100), nullable=False)
    stored_filename = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)

    def __init__(self, name: Any, description: Any, price: Any, category_id: Any, original_name: Any, stored_filename: Any) -> Any:
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.original_name = original_name
        self.stored_filename = stored_filename

    def json(self) -> Any:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category_id": self.category_id,
            "original_name": self.original_name,
            "stored_filename": self.stored_filename,
        }

    @classmethod
    def get_all_active_products(cls: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None)).all()

    @classmethod
    def find_product(cls: Any, id: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None), cls.id == id).first()

    @classmethod
    def find_by_name(cls: Any, name: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None), cls.name == name).first()

    def save_product(self) -> Any:
        db.session.add(self)
        db.session.commit()

    def update_product(self, **kwargs: Any) -> Any:
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        db.session.commit()

    def delete_product(self) -> Any:
        self.deleted_at = datetime.now(timezone.utc)
        db.session.commit()


# Eventos para created_at / updated_at
@event.listens_for(ProductModel, "before_insert")
def before_insert(mapper: Any, connection: Any, target: Any) -> Any:
    target.created_at = datetime.now(timezone.utc)
    target.updated_at = datetime.now(timezone.utc)


@event.listens_for(ProductModel, "before_update")
def before_update(mapper: Any, connection: Any, target: Any) -> Any:
    target.updated_at = datetime.now(timezone.utc)
