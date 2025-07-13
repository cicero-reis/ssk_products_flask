from src.application.category.commands.abstract.delete_category_command_abstract import DeleteCategoryCommandAbstract
from src.application.category.events.abstract.event_category_publisher_abstract import EventCategoryPublisherAbstract

class DeleteCategoryCommand(DeleteCategoryCommandAbstract):
    def __init__(self, repo: DeleteCategoryCommandAbstract, event: EventCategoryPublisherAbstract):
        self.repo = repo
        self.event = event

    def handle(self, id):
        
        category = self.repo.delete(id)
        
        if not category:
            return None, f'Category id {id} not found'

        self.event.publish_event("category_deleted", {"category_id": id})

        return True, None
