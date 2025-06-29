import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    S3_PUBLIC_URL = os.getenv("S3_PUBLIC_URL", "")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "sskproduct")

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USERNAME', 'root')}:" 
        f"{os.getenv('DB_PASSWORD', 'root')}@"
        f"{os.getenv('DB_HOST', 'mysql')}/"
        f"{os.getenv('DB_DATABASE', 'ssk_product')}?charset=utf8mb4"
    )

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USERNAME', 'root')}:" 
        f"{os.getenv('DB_PASSWORD', 'root')}@"
        f"{os.getenv('DB_HOST', 'db')}:{os.getenv('DB_PORT', '3306')}/"
        f"{os.getenv('DB_DATABASE', 'ssk_product')}?charset=utf8mb4"
    )

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
