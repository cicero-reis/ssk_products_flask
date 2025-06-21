from datetime import datetime
from extensions import db

class ProducEvent(db.Model):
    __tablename__ = 'product_event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    data = db.Column(db.JSON, nullable=False)
    timestamp = db.Column(db.TIMESTAMP, default=datetime.utcnow)

    def json(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "user_id": self.user_id,
            "event_type": self.event_type,
            "data": self.data,
            "timestamp": self.timestamp.isoformat()
        }
