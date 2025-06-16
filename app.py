from flask import Flask
from extensions import db, migrate
import os

def create_app():
    app = Flask(__name__)

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
    from presentation.routes import product_bp
    app.register_blueprint(product_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    print("➡ Criando o app Flask e registrando rotas...")
    app = create_app()
    env = os.getenv("FLASK_ENV", "development")  # lê diretamente o ambiente
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "1") == "1"
    print(f"🚀 Servidor rodando em http://0.0.0.0:{port} (debug={debug}, env={env})")
    app.run(host="0.0.0.0", port=port, debug=debug)
