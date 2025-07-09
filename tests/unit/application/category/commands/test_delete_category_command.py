import unittest
from unittest.mock import Mock

from application.category.commands.delete_category_command import DeleteCategoryCommand


class TestDeleteCategoryCommand(unittest.TestCase):
    def setUp(self):
        # Criar mocks para as dependências
        self.mock_repo = Mock()
        self.mock_event_publisher = Mock()
        
        # Instanciar o comando com os mocks
        self.command = DeleteCategoryCommand(
            repo=self.mock_repo,
            event=self.mock_event_publisher
        )
        
    def test_handle_should_delete_category_and_publish_event(self):
        # Arrange
        category_id = 1
        
        # Configure o mock para retornar True (sucesso na exclusão)
        self.mock_repo.delete.return_value = True
        
        # Act
        result, error = self.command.handle(category_id)
        
        # Assert
        self.mock_repo.delete.assert_called_once_with(category_id)
        self.mock_event_publisher.publish_event.assert_called_once_with(
            "category_deleted", 
            {"category_id": category_id}
        )
        
        self.assertTrue(result)
        self.assertIsNone(error)
        
    def test_handle_should_return_error_when_category_not_found(self):
        # Arrange
        category_id = 999
        
        # Configure o mock para retornar None (falha na exclusão)
        self.mock_repo.delete.return_value = None
        
        # Act
        result, error = self.command.handle(category_id)
        
        # Assert
        self.mock_repo.delete.assert_called_once_with(category_id)
        self.mock_event_publisher.publish_event.assert_not_called()
        
        self.assertIsNone(result)
        self.assertEqual(error, f'Category id {category_id} not found')


if __name__ == '__main__':
    unittest.main()
