class DeleteCategoryCommandAbstract(DeleteCategoryCommandAbstract):
    def handle(self, category_id: int) -> None:
        """
        Deletes a category by its ID.
        
        :param category_id: The ID of the category to delete.
        :raises ValueError: If the category does not exist.
        """
        raise NotImplementedError("This method should be overridden in a subclass.")
