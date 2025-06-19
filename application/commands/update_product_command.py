from domain.repositories.update_product_repository_abstract import UpdateProductRepositoryAbstract
from application.commands.abstract.update_product_command_abstract import UpdateProductCommandAbstract

class UpdateProductCommand(UpdateProductCommandAbstract):
    def __init__(self, repo: UpdateProductRepositoryAbstract):
        self.repo = repo

    def handle(self, id, data):
        product = self.repo.update(id, data)
        if not product:
            return None, f'Product id {id} not found'
        return product.json(), None