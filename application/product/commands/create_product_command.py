from application.product.commands.abstract.create_product_command_abstract import CreateProductCommandAbstract
from domain.product.repositories.create_product_repository_abstract import CreateProductRepositoryAbstract
from application.product.events.abstract.event_product_publisher_abstract import EventProductPublisherAbstract
from application.product.dtos.product_dto import ProductDTO

class CreateProductCommand(CreateProductCommandAbstract):

    def __init__(self, repo: CreateProductRepositoryAbstract, event: EventProductPublisherAbstract):        
        self.repo = repo
        self.event = event

    def handle(self, data):

        product = self.repo.create(data)

        self.event.publish_event("product_created", {"product_id": product.id})

        dto = ProductDTO.from_entity(product)

        return dto.to_dict(), None