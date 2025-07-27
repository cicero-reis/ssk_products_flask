"""
Este arquivo contém fixtures e utilidades para os testes.
"""
import pytest
import sys
import os
from flask import Flask

# Adiciona o diretório raiz do projeto ao PYTHONPATH
# para que as importações funcionem corretamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.utils.app_context import create_test_app

@pytest.fixture
def app_config():
    """
    Fixture que fornece a configuração do app para os testes
    """
    return {
        'S3_PUBLIC_URL': 'https://s3.example.com',
        'S3_BUCKET_NAME': 'test-bucket'
    }

@pytest.fixture
def app():
    """
    Fixture que cria e fornece um app Flask para testes
    """
    app = create_test_app()
    return app

@pytest.fixture
def app_context(app):
    """
    Fixture que cria e ativa um contexto de aplicação Flask para os testes
    """
    with app.app_context():
        yield
