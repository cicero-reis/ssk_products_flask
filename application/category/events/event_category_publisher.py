from application.category.events.abstract.event_category_publisher_abstract import EventCategoryPublisherAbstract

class EventCategoryPublisher(EventCategoryPublisherAbstract):
    def publish_event(self, event_name: str, data: dict):
        print(f"Event published: {event_name} with data: {data}")