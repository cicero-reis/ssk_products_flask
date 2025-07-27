import os
from pymongo import MongoClient

mongo_client = None
db = None

def init_app(app):
    """
    Inicializa a conexão com o MongoDB usando o app Flask.
    Adiciona o cliente e o db ao app.extensions.
    """
    global mongo_client, db
    MONGO_HOST = app.config.get('MONGO_HOST', os.getenv('MONGO_HOST', 'ssk_mongodb'))
    MONGO_PORT = int(app.config.get('MONGO_PORT', os.getenv('MONGO_PORT', 27017)))
    MONGO_DB = app.config.get('MONGO_DB', os.getenv('MONGO_DB', 'ssk_orders'))
    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    mongo_client = MongoClient(MONGO_URI)
    db = mongo_client[MONGO_DB]
    app.extensions = getattr(app, 'extensions', {})
    app.extensions['mongo_client'] = mongo_client
    app.extensions['mongo_db'] = db

def get_collection(collection_name):
    """
    Retorna uma coleção do banco MongoDB.
    """
    print("Obtendo coleção:")
    global db
    if db is None:
        raise RuntimeError('MongoDB não inicializado. Chame init_app(app) primeiro.')
    return db[collection_name]
