from application.commands.abstract.create_product_command_abstract import CreateProductCommandAbstract
from domain.repositories.create_product_repository_abstract import CreateProductRepositoryAbstract

class CreateProductCommand(CreateProductCommandAbstract):

    def __init__(self, repo: CreateProductRepositoryAbstract):
        self.repo = repo

    def handle(self, data):
        product = self.repo.create(data)
        return product.json(), None