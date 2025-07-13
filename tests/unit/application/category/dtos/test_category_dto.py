import unittest

from src.application.category.dtos.category_dto import CategoryDto
from src.domain.category.entity.category_entity import CategoryEntity


class TestCategoryDto(unittest.TestCase):
    def test_from_entity(self):
        # Arrange
        category = CategoryEntity(id=1, name="Test Category", description="Test Description")
        
        # Act
        dto = CategoryDto.from_entity(category)
        
        # Assert
        self.assertEqual(dto.id, 1)
        self.assertEqual(dto.name, "Test Category")
        self.assertEqual(dto.description, "Test Description")
        
    def test_to_dict(self):
        # Arrange
        dto = CategoryDto(id=1, name="Test Category", description="Test Description")
        
        # Act
        result = dto.to_dict()
        
        # Assert
        expected = {
            "id": 1,
            "name": "Test Category",
            "description": "Test Description"
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
