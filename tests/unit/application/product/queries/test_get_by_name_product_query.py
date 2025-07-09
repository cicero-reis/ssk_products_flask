import unittest
from unittest.mock import Mock, patch

from application.product.queries.get_by_name_product_query import GetByNameProductQuery
from domain.product.entity.product_entity import ProductEntity
from tests.utils.stubs import ProductDTOStub


class TestGetByNameProductQuery(unittest.TestCase):
    def setUp(self):
        # Criar mock para a dependência
        self.mock_repo = Mock()
        
        # Instanciar a query com o mock
        self.query = GetByNameProductQuery(repo=self.mock_repo)
        
    @patch('application.product.queries.get_by_name_product_query.ProductDTO', ProductDTOStub)
    def test_handle_should_return_product_when_found(self):
        # Arrange
        product_name = "Test Product"
        mock_product = ProductEntity(
            id=1, 
            name=product_name, 
            description="Test Description",
            price=19.99,
            category_id=1,
            original_name="test.jpg",
            stored_filename="abc123.jpg"
        )
        
        # Configure o mock para retornar o produto
        self.mock_repo.get_by_name.return_value = mock_product
        
        # Act
        result, error = self.query.handle(product_name)
        
        # Assert
        self.mock_repo.get_by_name.assert_called_once_with(product_name)
        
        self.assertIsNone(error)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], product_name)
        self.assertEqual(result["description"], "Test Description")
        self.assertEqual(result["price"], 19.99)
        self.assertEqual(result["category_id"], 1)
        self.assertEqual(result["original_name"], "test.jpg")
        self.assertEqual(result["stored_filename"], "https://s3.example.com/test-bucket/abc123.jpg")
        
    @patch('application.product.queries.get_by_name_product_query.ProductDTO', ProductDTOStub)
    def test_handle_should_return_error_when_product_not_found(self):
        # Arrange
        product_name = "Non Existent Product"
        
        # Configure o mock para retornar None (produto não encontrado)
        self.mock_repo.get_by_name.return_value = None
        
        # Act
        result, error = self.query.handle(product_name)
        
        # Assert
        self.mock_repo.get_by_name.assert_called_once_with(product_name)
        
        self.assertIsNone(result)
        self.assertEqual(error, f'Product name {product_name} not found')


if __name__ == '__main__':
    unittest.main()
