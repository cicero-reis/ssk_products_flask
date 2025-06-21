from application.commands.abstract.create_product_command_abstract import CreateProductCommandAbstract
from domain.repositories.create_product_repository_abstract import CreateProductRepositoryAbstract
from application.events.abstract.event_publisher_abstract import EventPublisherAbstract

class CreateProductCommand(CreateProductCommandAbstract):

    def __init__(self, repo: CreateProductRepositoryAbstract, event: EventPublisherAbstract):        
        self.repo = repo
        self.event = event

    def handle(self, data):

        product = self.repo.create(data)

        self.event.publish_event("product_created", {"product_id": product.id})

        return product.json(), None