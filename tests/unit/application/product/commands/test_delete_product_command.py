import unittest
from unittest.mock import Mock

from src.application.product.commands.delete_product_command import DeleteProductCommand


class TestDeleteProductCommand(unittest.TestCase):
    def setUp(self):
        # Criar mock para a dependência
        self.mock_repo = Mock()
        
        # Instanciar o comando com o mock
        self.command = DeleteProductCommand(repo=self.mock_repo)
        
    def test_handle_should_delete_product_and_return_success(self):
        # Arrange
        product_id = 1
        
        # Configure o mock para retornar True (sucesso na exclusão)
        self.mock_repo.delete.return_value = True
        
        # Act
        result, error = self.command.handle(product_id)
        
        # Assert
        self.mock_repo.delete.assert_called_once_with(product_id)
        
        self.assertTrue(result)
        self.assertIsNone(error)
        
    def test_handle_should_return_error_when_product_not_found(self):
        # Arrange
        product_id = 999
        
        # Configure o mock para retornar None (falha na exclusão)
        self.mock_repo.delete.return_value = None
        
        # Act
        result, error = self.command.handle(product_id)
        
        # Assert
        self.mock_repo.delete.assert_called_once_with(product_id)
        
        self.assertIsNone(result)
        self.assertEqual(error, f'Product id {product_id} not found')


if __name__ == '__main__':
    unittest.main()
