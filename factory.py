from flask import Flask
import os
import logging
from extensions import db, migrate
from errors.handlers import register_error_handlers
from presentation.product_routes import product_bp
from presentation.category_routes import category_bp

def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)
    app.logger.info('Iniciando a aplicação Flask')

    env = os.getenv('FLASK_ENV', 'development')
    app.config['ENV'] = env

    if env == 'production':
        app.config.from_object('config.ProductionConfig')
    elif env == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(category_bp, url_prefix='/api')

    # Registrar handlers de erro
    register_error_handlers(app)

    return app
