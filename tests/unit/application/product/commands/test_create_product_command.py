import unittest
from unittest.mock import Mock, patch

from src.application.product.commands.create_product_command import CreateProductCommand
from src.domain.product.entity.product_entity import ProductEntity
from tests.utils.stubs import ProductDTOStub


class TestCreateProductCommand(unittest.TestCase):
    def setUp(self):
        # Criar mocks para as dependências
        self.mock_repo = Mock()
        self.mock_event_publisher = Mock()
        
        # Instanciar o comando com os mocks
        self.command = CreateProductCommand(
            repo=self.mock_repo,
            event=self.mock_event_publisher
        )
        
    @patch('src.application.product.commands.create_product_command.ProductDTO', ProductDTOStub)
    def test_handle_should_create_product_and_publish_event(self):
        
        data = {
            "name": "Test Product", 
            "description": "Test Description", 
            "price": 19.99,
            "category_id": 1,
            "original_name": "test.jpg",
            "stored_filename": "abc123.jpg"
        }
        
        mock_product = ProductEntity(
            id=1, 
            name=data["name"], 
            description=data["description"],
            price=data["price"],
            category_id=data["category_id"],
            original_name=data["original_name"],
            stored_filename=data["stored_filename"]
        )
        
        self.mock_repo.create.return_value = mock_product
        
        # Act
        result, error = self.command.handle(data)
        
        # Assert
        self.mock_repo.create.assert_called_once_with(data)
        self.mock_event_publisher.publish_event.assert_called_once_with(
            "product_created", 
            {"product_id": 1}
        )
        
        self.assertIsNone(error)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], data["name"])
        self.assertEqual(result["description"], data["description"])
        self.assertEqual(result["price"], data["price"])
        self.assertEqual(result["category_id"], data["category_id"])
        self.assertEqual(result["original_name"], data["original_name"])
        self.assertEqual(result["stored_filename"], "https://s3.example.com/test-bucket/abc123.jpg")
        
    @patch('src.application.product.commands.create_product_command.ProductDTO', ProductDTOStub)
    def test_handle_should_return_dto_dictionary_with_null_image_url_when_no_stored_filename(self):
        
        data = {
            "name": "Test Product", 
            "description": "Test Description", 
            "price": 19.99,
            "category_id": 1,
            "original_name": None,
            "stored_filename": None
        }
        
        mock_product = ProductEntity(
            id=1, 
            name=data["name"], 
            description=data["description"],
            price=data["price"],
            category_id=data["category_id"],
            original_name=data["original_name"],
            stored_filename=data["stored_filename"]
        )
        
        self.mock_repo.create.return_value = mock_product
        
        # Act
        result, error = self.command.handle(data)
        
        # Assert
        expected = {
            "id": 1,
            "name": "Test Product",
            "description": "Test Description",
            "price": 19.99,
            "category_id": 1,
            "original_name": None,
            "stored_filename": None
        }
        
        self.assertEqual(result["id"], expected["id"])
        self.assertEqual(result["name"], expected["name"])
        self.assertEqual(result["description"], expected["description"])
        self.assertEqual(result["price"], expected["price"])
        self.assertEqual(result["category_id"], expected["category_id"])
        self.assertEqual(result["original_name"], expected["original_name"])
        self.assertEqual(result["stored_filename"], None)


if __name__ == '__main__':
    unittest.main()
