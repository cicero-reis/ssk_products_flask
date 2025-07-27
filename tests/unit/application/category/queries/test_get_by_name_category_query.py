import unittest
from unittest.mock import Mock

from src.application.category.queries.get_by_name_category_query import GetByNameCategoryQuery
from src.domain.category.entity.category_entity import CategoryEntity


class TestGetByNameCategoryQuery(unittest.TestCase):
    def setUp(self):
        # Criar mock para a dependência
        self.mock_repo = Mock()
        
        # Instanciar a query com o mock
        self.query = GetByNameCategoryQuery(repo=self.mock_repo)
        
    def test_handle_should_return_category_when_found(self):
        # Arrange
        category_name = "Test Category"
        mock_category = CategoryEntity(
            id=1, 
            name=category_name, 
            description="Test Description"
        )
        
        # Configure o mock para retornar a categoria
        self.mock_repo.get_by_name.return_value = mock_category
        
        # Act
        result, error = self.query.handle(category_name)
        
        # Assert
        self.mock_repo.get_by_name.assert_called_once_with(category_name)
        
        self.assertIsNone(error)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], category_name)
        self.assertEqual(result["description"], "Test Description")
        
    def test_handle_should_return_error_when_category_not_found(self):
        # Arrange
        category_name = "Non Existent Category"
        
        # Configure o mock para retornar None (categoria não encontrada)
        self.mock_repo.get_by_name.return_value = None
        
        # Act
        result, error = self.query.handle(category_name)
        
        # Assert
        self.mock_repo.get_by_name.assert_called_once_with(category_name)
        
        self.assertIsNone(result)
        self.assertEqual(error, f'Category name {category_name} not found')


if __name__ == '__main__':
    unittest.main()
