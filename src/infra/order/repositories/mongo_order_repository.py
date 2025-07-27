from datetime import datetime
from typing import Any

from bson import ObjectId

from src.infra.models.order_mongo_model import OrderMongoModel


class MongoOrderRepository:
    def __init__(self, db: Any, collection_name: Any = "orders") -> Any:
        self.collection = db[collection_name]

    def get_all(self) -> Any:
        cursor = self.collection.find({"deleted_at": None})
        return [OrderMongoModel.from_dict(doc) for doc in cursor]

    def get_by_id(self, order_id: Any) -> Any:
        doc = self.collection.find_one({"_id": ObjectId(order_id), "deleted_at": None})
        return OrderMongoModel.from_dict(doc) if doc else None

    def create(self, data: Any) -> Any:
        now = datetime.utcnow()
        data["created_at"] = now
        data["updated_at"] = now
        data["deleted_at"] = None

        # Gera order_number sequencial por dia
        start = datetime(now.year, now.month, now.day)
        end = datetime(now.year, now.month, now.day, 23, 59, 59, 999999)
        count = self.collection.count_documents({
            "created_at": {"$gte": start, "$lte": end}
        })
        data["order_number"] = count + 1

        result = self.collection.insert_one(data)
        return self.get_by_id(result.inserted_id)

    def update(self, order_id: Any, data: Any) -> Any:
        data["updated_at"] = datetime.utcnow()
        result = self.collection.update_one({"_id": ObjectId(order_id)}, {"$set": data})
        return self.get_by_id(order_id) if result.modified_count else None

    def delete(self, order_id: Any) -> Any:
        result = self.collection.update_one({"_id": ObjectId(order_id)}, {"$set": {"deleted_at": datetime.utcnow()}})
        return result.modified_count > 0
