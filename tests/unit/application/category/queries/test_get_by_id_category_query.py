import unittest
from unittest.mock import Mock

from src.application.category.queries.get_by_id_category_query import GetByIdCategoryQuery
from src.domain.category.entity.category_entity import CategoryEntity


class TestGetByIdCategoryQuery(unittest.TestCase):
    def setUp(self):
        # Criar mock para o repositório
        self.mock_repo = Mock()
        
        # Instanciar a query com o mock
        self.query = GetByIdCategoryQuery(repo=self.mock_repo)
        
    def test_handle_should_return_category_when_found(self):
        # Arrange
        category_id = 1
        mock_category = CategoryEntity(
            id=category_id, 
            name="Test Category", 
            description="Test Description"
        )
        self.mock_repo.get_by_id.return_value = mock_category
        
        # Act
        result, error = self.query.handle(category_id)
        
        # Assert
        self.mock_repo.get_by_id.assert_called_once_with(category_id)
        self.assertIsNone(error)
        
        expected = {
            "id": 1,
            "name": "Test Category",
            "description": "Test Description"
        }
        self.assertEqual(result, expected)
        
    def test_handle_should_return_error_when_category_not_found(self):
        # Arrange
        category_id = 999
        self.mock_repo.get_by_id.return_value = None
        
        # Act
        result, error = self.query.handle(category_id)
        
        # Assert
        self.mock_repo.get_by_id.assert_called_once_with(category_id)
        self.assertIsNone(result)
        self.assertEqual(error, f'Category id {category_id} not found')


if __name__ == '__main__':
    unittest.main()
