from functools import wraps
from flask import request
from cerberus import Validator # type: ignore

def validate_nome_empty(field, value, error):
    cleaned_value = value.strip()  # Remove espaços em branco no início e no final
    if not cleaned_value:  # Verifica se o valor está vazio após a remoção de espaços em branco
        error(field, "O campo não pode estar vazio")
    elif value != cleaned_value:  # Verifica se houve espaços em branco extras no início ou no final
        error(field, "O campo não pode conter espaços em branco extras no início ou no final")

hotel_schema = {
    'nome': {'type': 'string', 'empty': False, 'required': True, 'validator': validate_nome_empty},
    'estrelas': {'type': 'float', 'required': True},
    'diaria': {'type': 'float', 'required': True},
    'cidade': {'type': 'string', 'empty': False, 'required': True},
}

def validate_json(schema):

    def decorator(func):

        @wraps(func)

        def wrapper(*args, **kwargs):

            if request.json is None:
                data = { }
            else:
                data = request.json

            v = Validator(schema)

            if v.validate(data):
                return func(*args, **kwargs)
            else:
                return {'error': v.errors}, 400
            
        return wrapper
    
    return decorator
