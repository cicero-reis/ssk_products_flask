from application.events.abstract.event_publisher_abstract import EventPublisherAbstract

class EventPublisher(EventPublisherAbstract):
    def publish_event(self, event_name: str, data: dict):
        print(f"Publishing event: {event_name} with data: {data}")