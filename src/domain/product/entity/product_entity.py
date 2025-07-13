class ProductEntity:
    def __init__(self, id: int, name: str, description: str, price: float, category_id: int, original_name: str, stored_filename: str):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.original_name = original_name
        self.stored_filename = stored_filename