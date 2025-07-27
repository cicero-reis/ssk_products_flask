from flask import Flask


def create_test_app():
    """
    Cria uma instância de aplicação Flask para testes
    """
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['S3_PUBLIC_URL'] = 'https://s3.example.com'
    app.config['S3_BUCKET_NAME'] = 'test-bucket'
    
    return app
