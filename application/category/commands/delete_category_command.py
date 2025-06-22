from application.category.commands.delete_category_command_abstract import DeleteCategoryCommandAbstract

class DeleteCategoryCommand(DeleteCategoryCommandAbstract):
    def __init__(self, repo: DeleteCategoryCommandAbstract, event: EventCategoryPublisherAbstract):
        self.repo = repo
        self.event = event

    def handle(self, category_id):
        self.repo.delete(category_id)
        self.event.publish_event("category_deleted", {"category_id": category_id})