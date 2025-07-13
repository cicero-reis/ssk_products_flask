import unittest
from unittest.mock import Mock, patch

from src.application.product.commands.update_product_command import UpdateProductCommand
from src.domain.product.entity.product_entity import ProductEntity
from tests.utils.stubs import ProductDTOStub


class TestUpdateProductCommand(unittest.TestCase):
    def setUp(self):
        # Criar mocks para as dependências
        self.mock_repo = Mock()
        self.mock_event_publisher = Mock()
        
        # Instanciar o comando com os mocks
        self.command = UpdateProductCommand(
            repo=self.mock_repo,
            event=self.mock_event_publisher
        )
        
    @patch('src.application.product.commands.update_product_command.ProductDTO', ProductDTOStub)
    def test_handle_should_update_product_and_publish_event(self):
        # Arrange
        product_id = 1
        data = {
            "name": "Updated Product", 
            "description": "Updated Description", 
            "price": 29.99,
            "category_id": 2,
            "original_name": "updated.jpg",
            "stored_filename": "def456.jpg"
        }
        
        mock_product = ProductEntity(
            id=product_id, 
            name=data["name"], 
            description=data["description"],
            price=data["price"],
            category_id=data["category_id"],
            original_name=data["original_name"],
            stored_filename=data["stored_filename"]
        )
        
        # Configure o mock para retornar sucesso e o produto atualizado
        self.mock_repo.update.return_value = (True, mock_product)
        
        # Act
        result, error = self.command.handle(product_id, data)
        
        # Assert
        self.mock_repo.update.assert_called_once_with(product_id, data)
        self.mock_event_publisher.publish_event.assert_called_once_with(
            "product_updated", 
            {"product_id": product_id}
        )
        
        self.assertIsNone(error)
        self.assertEqual(result["id"], product_id)
        self.assertEqual(result["name"], data["name"])
        self.assertEqual(result["description"], data["description"])
        self.assertEqual(result["price"], data["price"])
        self.assertEqual(result["category_id"], data["category_id"])
        self.assertEqual(result["original_name"], data["original_name"])
        self.assertEqual(result["stored_filename"], f"https://s3.example.com/test-bucket/{data['stored_filename']}")
        
    @patch('src.application.product.commands.update_product_command.ProductDTO', ProductDTOStub)
    def test_handle_should_return_error_when_product_not_found(self):
        # Arrange
        product_id = 999
        data = {
            "name": "Updated Product", 
            "description": "Updated Description"
        }
        
        # Configure o mock para retornar falha
        self.mock_repo.update.return_value = (False, None)
        
        # Act
        result, error = self.command.handle(product_id, data)
        
        # Assert
        self.mock_repo.update.assert_called_once_with(product_id, data)
        self.mock_event_publisher.publish_event.assert_not_called()
        
        self.assertIsNone(result)
        self.assertEqual(error, f'Product id {product_id} not found')


if __name__ == '__main__':
    unittest.main()
