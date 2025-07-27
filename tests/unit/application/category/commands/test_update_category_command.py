import unittest
from unittest.mock import Mock

from src.application.category.commands.update_category_command import UpdateCategoryCommand
from src.domain.category.entity.category_entity import CategoryEntity


class TestUpdateCategoryCommand(unittest.TestCase):
    def setUp(self):
        # Criar mocks para as dependências
        self.mock_repo = Mock()
        self.mock_event_publisher = Mock()
        
        # Instanciar o comando com os mocks
        self.command = UpdateCategoryCommand(
            repo=self.mock_repo,
            event=self.mock_event_publisher
        )
        
    def test_handle_should_update_category_and_publish_event(self):
        # Arrange
        category_id = 1
        data = {"name": "Updated Category", "description": "Updated Description"}
        mock_category = CategoryEntity(id=category_id, name=data["name"], description=data["description"])
        
        # Configure o mock para retornar sucesso e a categoria atualizada
        self.mock_repo.update.return_value = (True, mock_category)
        
        # Act
        result, error = self.command.handle(category_id, data)
        
        # Assert
        self.mock_repo.update.assert_called_once_with(category_id, data)
        self.mock_event_publisher.publish_event.assert_called_once_with(
            "category_updated", 
            {"category_id": category_id}
        )
        
        self.assertIsNone(error)
        self.assertEqual(result["id"], category_id)
        self.assertEqual(result["name"], data["name"])
        self.assertEqual(result["description"], data["description"])
        
    def test_handle_should_return_error_when_category_not_found(self):
        # Arrange
        category_id = 999
        data = {"name": "Updated Category", "description": "Updated Description"}
        
        # Configure o mock para retornar falha
        self.mock_repo.update.return_value = (False, None)
        
        # Act
        result, error = self.command.handle(category_id, data)
        
        # Assert
        self.mock_repo.update.assert_called_once_with(category_id, data)
        self.mock_event_publisher.publish_event.assert_not_called()
        
        self.assertIsNone(result)
        self.assertEqual(error, f'Category id {category_id} not found')


if __name__ == '__main__':
    unittest.main()
