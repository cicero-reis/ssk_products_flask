import unittest
from unittest.mock import patch

from src.domain.product.entity.product_entity import ProductEntity
from tests.utils.stubs import ProductDTOStub


class TestProductDTO(unittest.TestCase):

    def test_from_entity(self):
        # Arrange
        product = ProductEntity(
            id=1, 
            name="Test Product", 
            description="Test Description",
            price=19.99,
            category_id=1,
            original_name="test.jpg",
            stored_filename="abc123.jpg"
        )
        
        # Act
        dto = ProductDTOStub.from_entity(product)
        
        # Assert
        self.assertEqual(dto.id, 1)
        self.assertEqual(dto.name, "Test Product")
        self.assertEqual(dto.description, "Test Description")
        self.assertEqual(dto.price, 19.99)
        self.assertEqual(dto.category_id, 1)
        self.assertEqual(dto.original_name, "test.jpg")
        self.assertEqual(dto.stored_filename, "abc123.jpg")
        
    def test_to_dict_with_stored_filename(self):
        # Arrange
        dto = ProductDTOStub(
            id=1, 
            name="Test Product", 
            description="Test Description",
            price=19.99,
            category_id=1,
            original_name="test.jpg",
            stored_filename="abc123.jpg"
        )
        
        # Act
        result = dto.to_dict()
        
        # Assert
        expected = {
            "id": 1,
            "name": "Test Product",
            "description": "Test Description",
            "price": 19.99,
            "category_id": 1,
            "original_name": "test.jpg",
            "stored_filename": "https://s3.example.com/test-bucket/abc123.jpg"
        }
        self.assertEqual(result, expected)
        
    def test_to_dict_without_stored_filename(self):
        # Arrange
        dto = ProductDTOStub(
            id=1, 
            name="Test Product", 
            description="Test Description",
            price=19.99,
            category_id=1,
            original_name=None,
            stored_filename=None
        )
        
        # Act
        result = dto.to_dict()
        
        # Assert
        expected = {
            "id": 1,
            "name": "Test Product",
            "description": "Test Description",
            "price": 19.99,
            "category_id": 1,
            "original_name": None,
            "stored_filename": None
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
