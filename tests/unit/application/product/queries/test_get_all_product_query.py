import unittest
from unittest.mock import Mock, patch

from application.product.queries.get_all_product_query import GetAllProductQuery
from domain.product.entity.product_entity import ProductEntity
from tests.utils.stubs import ProductDTOStub


class TestGetAllProductQuery(unittest.TestCase):
    def setUp(self):
        # Criar mock para a dependência
        self.mock_repo = Mock()
        
        # Instanciar a query com o mock
        self.query = GetAllProductQuery(repo=self.mock_repo)
        
    @patch('application.product.queries.get_all_product_query.ProductDTO', ProductDTOStub)
    def test_handle_should_return_all_products(self):
        # Arrange
        mock_products = [
            ProductEntity(
                id=1, 
                name="Product 1", 
                description="Description 1",
                price=19.99,
                category_id=1,
                original_name="test1.jpg",
                stored_filename="abc123.jpg"
            ),
            ProductEntity(
                id=2, 
                name="Product 2", 
                description="Description 2",
                price=29.99,
                category_id=2,
                original_name="test2.jpg",
                stored_filename="def456.jpg"
            ),
            ProductEntity(
                id=3, 
                name="Product 3", 
                description="Description 3",
                price=39.99,
                category_id=1,
                original_name=None,
                stored_filename=None
            )
        ]
        
        # Configure o mock para retornar a lista de produtos
        self.mock_repo.get_all.return_value = mock_products
        
        # Act
        result, error = self.query.handle()
        
        # Assert
        self.mock_repo.get_all.assert_called_once()
        
        self.assertIsNone(error)
        self.assertEqual(len(result), 3)
        
        # Verifica o primeiro produto
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["name"], "Product 1")
        self.assertEqual(result[0]["description"], "Description 1")
        self.assertEqual(result[0]["price"], 19.99)
        self.assertEqual(result[0]["category_id"], 1)
        self.assertEqual(result[0]["original_name"], "test1.jpg")
        self.assertEqual(result[0]["stored_filename"], "https://s3.example.com/test-bucket/abc123.jpg")
        
        # Verifica o segundo produto
        self.assertEqual(result[1]["id"], 2)
        self.assertEqual(result[1]["name"], "Product 2")
        self.assertEqual(result[1]["stored_filename"], "https://s3.example.com/test-bucket/def456.jpg")
        
        # Verifica o terceiro produto
        self.assertEqual(result[2]["id"], 3)
        self.assertEqual(result[2]["name"], "Product 3")
        self.assertEqual(result[2]["stored_filename"], None)
        
    @patch('application.product.queries.get_all_product_query.ProductDTO', ProductDTOStub)
    def test_handle_should_return_empty_list_when_no_products(self):
        # Arrange
        # Configure o mock para retornar uma lista vazia
        self.mock_repo.get_all.return_value = []
        
        # Act
        result, error = self.query.handle()
        
        # Assert
        self.mock_repo.get_all.assert_called_once()
        
        self.assertIsNone(error)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
