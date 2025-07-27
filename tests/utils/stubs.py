"""
Classes de stub (substitutos) para testes unitários.
Estas implementações substituem classes reais que dependem de 
recursos externos como o contexto da aplicação Flask.
"""

class ProductDTOStub:
    """
    Versão de stub do ProductDTO que não depende do current_app do Flask.
    Implementação completamente independente, sem herdar da classe original.
    """
    
    # Configurações de exemplo para testes
    S3_PUBLIC_URL = 'https://s3.example.com'
    S3_BUCKET_NAME = 'test-bucket'
    
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
        """
        Cria um DTO a partir de uma entidade.
        """
        return ProductDTOStub(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id,
            original_name=product.original_name,
            stored_filename=product.stored_filename
        )
    
    def to_dict(self):
        """
        Converte o DTO para um dicionário.
        """
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
        """
        Versão independente que não depende do current_app
        """
        if self.stored_filename:
            return f"{self.S3_PUBLIC_URL}/{self.S3_BUCKET_NAME}/{self.stored_filename}"
        
        return None
