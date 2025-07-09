import unittest
from unittest.mock import Mock

from application.category.queries.get_all_category_query import GetAllCategoryQuery
from domain.category.entity.category_entity import CategoryEntity


class TestGetAllCategoryQuery(unittest.TestCase):
    def setUp(self):
        # Criar mock para a dependência
        self.mock_repo = Mock()
        
        # Instanciar a query com o mock
        self.query = GetAllCategoryQuery(repo=self.mock_repo)
        
    def test_handle_should_return_all_categories(self):
        # Arrange
        mock_categories = [
            CategoryEntity(id=1, name="Category 1", description="Description 1"),
            CategoryEntity(id=2, name="Category 2", description="Description 2"),
            CategoryEntity(id=3, name="Category 3", description="Description 3")
        ]
        
        # Configure o mock para retornar a lista de categorias
        self.mock_repo.get_all_categories.return_value = mock_categories
        
        # Act
        result, error = self.query.handle()
        
        # Assert
        self.mock_repo.get_all_categories.assert_called_once()
        
        self.assertIsNone(error)
        self.assertEqual(len(result), 3)
        
        # Verifica o primeiro item
        self.assertEqual(result[0]["id"], 1)
        self.assertEqual(result[0]["name"], "Category 1")
        self.assertEqual(result[0]["description"], "Description 1")
        
        # Verifica o segundo item
        self.assertEqual(result[1]["id"], 2)
        self.assertEqual(result[1]["name"], "Category 2")
        self.assertEqual(result[1]["description"], "Description 2")
        
        # Verifica o terceiro item
        self.assertEqual(result[2]["id"], 3)
        self.assertEqual(result[2]["name"], "Category 3")
        self.assertEqual(result[2]["description"], "Description 3")
        
    def test_handle_should_return_empty_list_when_no_categories(self):
        # Arrange
        # Configure o mock para retornar uma lista vazia
        self.mock_repo.get_all_categories.return_value = []
        
        # Act
        result, error = self.query.handle()
        
        # Assert
        self.mock_repo.get_all_categories.assert_called_once()
        
        self.assertIsNone(error)
        self.assertEqual(result, [])
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
