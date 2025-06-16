#from domain.entities.product_entitie import ProductEntitie
from datetime import datetime, timezone
from sqlalchemy import event # type: ignore
from extensions import db

class ProductModel(db.Model):
    
    __tablename__ = 'product'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    category = db.Column(db.String(100))
    image = db.Column(db.String(100))
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)

    @classmethod
    def before_insert(cls, mapper, connection, target):
        target.created_at = datetime.now(timezone.utc)
        target.updated_at = datetime.now(timezone.utc)

    @classmethod
    def before_update(cls, mapper, connection, target):
        target.updated_at = datetime.now(timezone.utc)

    @classmethod
    def before_delete(cls, mapper, connection, target):
        target.deleted_at = datetime.now(timezone.utc)
        target.is_deleted = False
        db.session.add(target)
        db.session.commit()

    def __init__(self, name, description, price, category, image):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.image = image

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'image': self.image
        }
    
    @classmethod
    def get_all_active_products(cls):
        return cls.query.all()
    
    @classmethod
    def find_product(cls, id):
        return cls.query.filter(cls.deleted_at == None, cls.id == id).first()
    
    def save_product(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_product(self, **wargs):
        for attr, value in wargs.items():
            setattr(self, attr, value)
        db.session.commit()
        
    @classmethod
    def delete_product(self):
        self.deleted_at = datetime.now(timezone.utc)
        db.session.commit()

event.listen(ProductModel, 'before_insert', ProductModel.before_insert)
event.listen(ProductModel, 'before_update', ProductModel.before_update)
event.listen(ProductModel, 'before_delete', ProductModel.before_delete)