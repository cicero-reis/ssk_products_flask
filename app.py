from factory import create_app
import os

if __name__ == '__main__':
    app = create_app()
    env = os.getenv("FLASK_ENV", "development")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "1") == "1"
    print(f"🚀 Servidor rodando em http://0.0.0.0:{port} (debug={debug}, env={env})")
    app.run(host="0.0.0.0", port=port, debug=debug)
