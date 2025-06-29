from flask import current_app

class ProductDTO:
    def __init__(self, id, name, description, price, category_id, original_name, stored_filename):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.original_name = original_name
        self.stored_filename = stored_filename

    @staticmethod
    def from_entity(product):
        return ProductDTO(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id,
            original_name=product.original_name,
            stored_filename=product.stored_filename
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category_id": self.category_id,
            "original_name": self.original_name,
            "stored_filename": self.get_image_url()
        }

    def get_image_url(self):

        if self.stored_filename:
            return f"{current_app.config['S3_PUBLIC_URL']}/{current_app.config['S3_BUCKET_NAME']}/{self.stored_filename}"

        return None
