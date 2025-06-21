from domain.product.repositories.update_product_repository_abstract import UpdateProductRepositoryAbstract
from application.product.commands.abstract.update_product_command_abstract import UpdateProductCommandAbstract
from application.product.dtos.product_dto import ProductDTO

class UpdateProductCommand(UpdateProductCommandAbstract):
    def __init__(self, repo: UpdateProductRepositoryAbstract):
        self.repo = repo

    def handle(self, id, data):
        product = self.repo.update(id, data)

        if not product:
            return None, f'Product id {id} not found'

        dto = ProductDTO.from_entity(product)

        return dto.to_dict(), None

        