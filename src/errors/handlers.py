from flask import jsonify
from sqlalchemy.exc import OperationalError


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"message": "Recurso não encontrado.", "status": 404}), 404

    @app.errorhandler(OperationalError)
    def handle_db_error(error):
        return jsonify(
            {
                "message": "Erro ao conectar ao banco de dados. Tente novamente mais tarde.",
                "status": 500,
            }
        ), 500

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify(
            {"message": "Ocorreu um erro interno no servidor. Tente novamente.", "status": 500}
        ), 500
