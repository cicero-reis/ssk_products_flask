from typing import Any
from datetime import datetime, timezone

from sqlalchemy import event  # type: ignore

from extensions import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)

    def __init__(self, name: Any, description: Any) -> Any:
        self.name = name
        self.description = description

    def json(self) -> Any:
        return {"id": self.id, "name": self.name, "description": self.description}

    @classmethod
    def get_all_categories(cls: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None)).all()

    @classmethod
    def find_by_id(cls: Any, id: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None), cls.id == id).first()

    @classmethod
    def find_by_name(cls: Any, name: Any) -> Any:
        return cls.query.filter(cls.deleted_at.is_(None), cls.name == name).first()

    def save_category(self) -> Any:
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs: Any) -> Any:
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        db.session.commit()

    def delete(self) -> Any:
        self.deleted_at = datetime.now(timezone.utc)
        db.session.commit()


# Eventos para created_at / updated_at
@event.listens_for(CategoryModel, "before_insert")
def before_insert(mapper: Any, connection: Any, target: Any) -> Any:
    target.created_at = datetime.now(timezone.utc)
    target.updated_at = datetime.now(timezone.utc)


@event.listens_for(CategoryModel, "before_update")
def before_update(mapper: Any, connection: Any, target: Any) -> Any:
    target.updated_at = datetime.now(timezone.utc)
