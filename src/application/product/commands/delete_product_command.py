from src.domain.product.repositories.delete_product_repository_abstract import DeleteProductRepositoryAbstract
from src.application.product.commands.abstract.delete_product_command_abstract import DeleteProductCommandAbstract

class DeleteProductCommand(DeleteProductCommandAbstract):

    def __init__(self, repo: DeleteProductRepositoryAbstract):
        self.repo = repo

    def handle(self, id):
        product = self.repo.delete(id)
        if not product:
            return None, f'Product id {id} not found'
        return True, None