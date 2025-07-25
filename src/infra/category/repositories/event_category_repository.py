import logging

from extensions import db
from src.domain.category.repositories.event_category_repository_abstract import (
    EventCategoryRepositoryAbstract,
)
from src.infra.models.category_event import CategoryEvent

logger = logging.getLogger(__name__)

class EventCategoryRepository(EventCategoryRepositoryAbstract):
    def save_event(self, event_type, data, user_id=0):
        event = CategoryEvent(
            category_id=data.id,
            user_id=user_id,
            event_type=event_type,
            data=data.json(),
        )
        db.session.add(event)
        db.session.commit()
        return event

    def get_events(self, category_id):
        return (
            CategoryEvent.query.filter_by(category_id=category_id)
            .order_by(CategoryEvent.timestamp.desc())
            .all()
        )
