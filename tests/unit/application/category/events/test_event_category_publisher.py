import unittest
from unittest.mock import patch
from io import StringIO
import sys

from application.category.events.event_category_publisher import EventCategoryPublisher


class TestEventCategoryPublisher(unittest.TestCase):
    def test_publish_event(self):
        # Arrange
        publisher = EventCategoryPublisher()
        event_name = "test_event"
        data = {"test_key": "test_value"}
        
        # Use StringIO para capturar o output do print
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Act
        publisher.publish_event(event_name, data)
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Assert
        expected_output = f"Event published: {event_name} with data: {data}\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Alternativa usando mock para testar o método
    def test_publish_event_with_mock(self):
        # Arrange
        publisher = EventCategoryPublisher()
        event_name = "test_event"
        data = {"test_key": "test_value"}
        
        # Act / Assert
        with patch("builtins.print") as mock_print:
            publisher.publish_event(event_name, data)
            mock_print.assert_called_once_with(f"Event published: {event_name} with data: {data}")


if __name__ == '__main__':
    unittest.main()
