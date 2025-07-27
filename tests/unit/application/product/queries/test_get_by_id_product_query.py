import unittest
from unittest.mock import Mock, patch

from src.application.product.queries.get_by_id_product_query import GetByIdProductQuery
from src.domain.product.entity.product_entity import ProductEntity
from tests.utils.stubs import ProductDTOStub


class TestGetByIdProductQuery(unittest.TestCase):
    def setUp(self):
        # Criar mock para a dependência
        self.mock_repo = Mock()
        
        # Instanciar a query com o mock
        self.query = GetByIdProductQuery(repo=self.mock_repo)
        
    @patch('src.application.product.queries.get_by_id_product_query.ProductDTO', ProductDTOStub)
    def test_handle_should_return_product_when_found(self):
        # Arrange
        product_id = 1
        mock_product = ProductEntity(
            id=product_id, 
            name="Test Product", 
            description="Test Description",
            price=19.99,
            category_id=1,
            original_name="test.jpg",
            stored_filename="abc123.jpg"
        )
        
        # Configure o mock para retornar o produto
        self.mock_repo.get_by_id.return_value = mock_product
        
        # Act
        result, error = self.query.handle(product_id)
        
        # Assert
        self.mock_repo.get_by_id.assert_called_once_with(product_id)
        
        self.assertIsNone(error)
        self.assertEqual(result["id"], product_id)
        self.assertEqual(result["name"], "Test Product")
        self.assertEqual(result["description"], "Test Description")
        self.assertEqual(result["price"], 19.99)
        self.assertEqual(result["category_id"], 1)
        self.assertEqual(result["original_name"], "test.jpg")
        self.assertEqual(result["stored_filename"], "https://s3.example.com/test-bucket/abc123.jpg")
        
    @patch('src.application.product.queries.get_by_id_product_query.ProductDTO', ProductDTOStub)
    def test_handle_should_return_error_when_product_not_found(self):
        # Arrange
        product_id = 999
        
        # Configure o mock para retornar None (produto não encontrado)
        self.mock_repo.get_by_id.return_value = None
        
        # Act
        result, error = self.query.handle(product_id)
        
        # Assert
        self.mock_repo.get_by_id.assert_called_once_with(product_id)
        
        self.assertIsNone(result)
        self.assertEqual(error, f'Product id {product_id} not found')


if __name__ == '__main__':
    unittest.main()
