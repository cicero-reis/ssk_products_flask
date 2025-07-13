from src.application.product.events.abstract.event_product_publisher_abstract import (
    EventProductPublisherAbstract,
)


class EventProductPublisher(EventProductPublisherAbstract):
    def publish_event(self, event_name: str, data: dict):
        print(f"Publishing event: {event_name} with data: {data}")
