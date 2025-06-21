from infra.models.product_event import ProducEvent
from extensions import db
from domain.repositories.product_event_store_repository_abstract import ProductEventStoreRepositoryAbstract

class ProductEventStoreRepository(ProductEventStoreRepositoryAbstract):
    def save_event(self, event_type, data, user_id=0):
        event = ProducEvent(
            product_id=data.id,
            user_id=user_id,
            event_type=event_type,
            data=data.json()
        )
        db.session.add(event)
        db.session.commit()
        return event

    def get_events_for_aggregate(self, product_id):
        return ProducEvent.query.filter_by(product_id=product_id).order_by(ProducEvent.timestamp).all()
