import unittest
from unittest.mock import Mock, patch

from src.application.category.commands.create_category_command import CreateCategoryCommand
from src.domain.category.entity.category_entity import CategoryEntity


class TestCreateCategoryCommand(unittest.TestCase):
    def setUp(self):
        # Criar mocks para as dependências
        self.mock_repo = Mock()
        self.mock_event_publisher = Mock()
        
        # Instanciar o comando com os mocks
        self.command = CreateCategoryCommand(
            repo=self.mock_repo,
            event=self.mock_event_publisher
        )
        
    def test_handle_should_create_category_and_publish_event(self):
        # Arrange
        data = {"name": "Test Category", "description": "Test Description"}
        mock_category = CategoryEntity(id=1, name=data["name"], description=data["description"])
        self.mock_repo.create.return_value = mock_category
        
        # Act
        result, error = self.command.handle(data)
        
        # Assert
        self.mock_repo.create.assert_called_once_with(data)
        self.mock_event_publisher.publish_event.assert_called_once_with(
            "category_created", 
            {"category_id": 1}
        )
        
        self.assertIsNone(error)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], data["name"])
        self.assertEqual(result["description"], data["description"])
        
    def test_handle_should_return_dto_dictionary(self):
        # Arrange
        data = {"name": "Test Category", "description": "Test Description"}
        mock_category = CategoryEntity(id=1, name=data["name"], description=data["description"])
        self.mock_repo.create.return_value = mock_category
        
        # Act
        result, error = self.command.handle(data)
        
        # Assert
        expected = {
            "id": 1,
            "name": "Test Category",
            "description": "Test Description"
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
