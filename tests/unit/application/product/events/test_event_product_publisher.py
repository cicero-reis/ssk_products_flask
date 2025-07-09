import unittest
from unittest.mock import patch
from io import StringIO
import sys

from application.product.events.event_product_publisher import EventProductPublisher


class TestEventProductPublisher(unittest.TestCase):
    def test_publish_event(self):
        # Arrange
        publisher = EventProductPublisher()
        event_name = "test_event"
        data = {"product_id": 1, "status": "created"}
        
        # Use StringIO para capturar o output do print
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Act
        publisher.publish_event(event_name, data)
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Assert
        expected_output = f"Publishing event: {event_name} with data: {data}\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Alternativa usando mock para testar o método
    def test_publish_event_with_mock(self):
        # Arrange
        publisher = EventProductPublisher()
        event_name = "test_event"
        data = {"product_id": 1, "status": "updated"}
        
        # Act / Assert
        with patch("builtins.print") as mock_print:
            publisher.publish_event(event_name, data)
            mock_print.assert_called_once_with(f"Publishing event: {event_name} with data: {data}")


if __name__ == '__main__':
    unittest.main()
