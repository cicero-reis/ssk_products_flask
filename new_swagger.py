from flask import jsonify
from flask_swagger_ui import get_swaggerui_blueprint

# Definição da especificação OpenAPI como um dicionário
SWAGGER_DEFINITION = {
    "openapi": "3.0.0",
    "info": {
        "title": "SSK Products API",
        "description": "API para gerenciamento de produtos e categorias",
        "version": "1.0.0"
    },
    "servers": [
        {
            "url": "/api",
            "description": "API Server"
        }
    ],
    "tags": [
        {
            "name": "Categorias",
            "description": "Gerenciamento de categorias"
        },
        {
            "name": "Produtos",
            "description": "Gerenciamento de produtos"
        }
    ],
    "paths": {
        "/categories": {
            "get": {
                "tags": ["Categorias"],
                "summary": "Lista todas as categorias",
                "responses": {
                    "200": {
                        "description": "Lista de categorias",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "categories": {
                                            "type": "array",
                                            "items": {"$ref": "#/components/schemas/Category"}
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Erro na requisição",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Categorias"],
                "summary": "Cria uma nova categoria",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/CategoryInput"}
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Categoria criada",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "category": {"$ref": "#/components/schemas/Category"}
                                    }
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Erro na requisição",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            }
        },
        "/categories/{id}": {
            "get": {
                "tags": ["Categorias"],
                "summary": "Obtém uma categoria específica",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Categoria encontrada",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "category": {"$ref": "#/components/schemas/Category"}
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Categoria não encontrada",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": ["Categorias"],
                "summary": "Atualiza uma categoria",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/CategoryInput"}
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Categoria atualizada",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "category": {"$ref": "#/components/schemas/Category"}
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Categoria não encontrada",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            },
            "delete": {
                "tags": ["Categorias"],
                "summary": "Remove uma categoria",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Categoria removida",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {
                                            "type": "string",
                                            "example": "Categoria removida com sucesso"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Categoria não encontrada",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            },
            "patch": {
                "tags": ["Categorias"],
                "summary": "Atualiza parcialmente uma categoria",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/CategoryPatchInput"}
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Categoria atualizada",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "category": {"$ref": "#/components/schemas/Category"}
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Categoria não encontrada",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            }
        },
        "/products": {
            "get": {
                "tags": ["Produtos"],
                "summary": "Lista todos os produtos",
                "responses": {
                    "200": {
                        "description": "Lista de produtos",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "products": {
                                            "type": "array",
                                            "items": {"$ref": "#/components/schemas/Product"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Produtos"],
                "summary": "Cria um novo produto",
                "requestBody": {
                    "content": {
                        "multipart/form-data": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "description": "Nome do produto"
                                    },
                                    "description": {
                                        "type": "string",
                                        "description": "Descrição do produto"
                                    },
                                    "price": {
                                        "type": "number",
                                        "format": "float",
                                        "description": "Preço do produto"
                                    },
                                    "category_id": {
                                        "type": "integer",
                                        "description": "ID da categoria"
                                    },
                                    "image": {
                                        "type": "string",
                                        "format": "binary",
                                        "description": "Imagem do produto"
                                    }
                                },
                                "required": ["name", "description", "price", "category_id"]
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Produto criado",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "product": {"$ref": "#/components/schemas/Product"}
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/products/{id}": {
            "get": {
                "tags": ["Produtos"],
                "summary": "Obtém um produto específico",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Produto encontrado",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "product": {"$ref": "#/components/schemas/Product"}
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Produto não encontrado",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            },
            "put": {
                "tags": ["Produtos"],
                "summary": "Atualiza um produto",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/ProductInput"}
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Produto atualizado",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "product": {"$ref": "#/components/schemas/Product"}
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Produto não encontrado",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            },
            "delete": {
                "tags": ["Produtos"],
                "summary": "Remove um produto",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Produto removido",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "message": {
                                            "type": "string",
                                            "example": "Produto removido com sucesso"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Produto não encontrado",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            },
            "patch": {
                "tags": ["Produtos"],
                "summary": "Atualiza parcialmente um produto",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "schema": {"type": "integer"}
                    }
                ],
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/ProductPatchInput"}
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Produto atualizado",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "product": {"$ref": "#/components/schemas/Product"}
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Produto não encontrado",
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Error"}
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "schemas": {
            "Category": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID único da categoria"
                    },
                    "name": {
                        "type": "string",
                        "description": "Nome da categoria"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição da categoria"
                    }
                }
            },
            "CategoryInput": {
                "type": "object",
                "required": ["name", "description"],
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome da categoria"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição da categoria"
                    }
                }
            },
            "CategoryPatchInput": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome da categoria"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição da categoria"
                    }
                }
            },
            "Product": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID único do produto"
                    },
                    "name": {
                        "type": "string",
                        "description": "Nome do produto"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição do produto"
                    },
                    "price": {
                        "type": "number",
                        "format": "float",
                        "description": "Preço do produto"
                    },
                    "category_id": {
                        "type": "integer",
                        "description": "ID da categoria do produto"
                    },
                    "original_name": {
                        "type": "string",
                        "description": "Nome original da imagem do produto"
                    },
                    "stored_filename": {
                        "type": "string",
                        "description": "URL da imagem do produto no S3"
                    }
                }
            },
            "ProductInput": {
                "type": "object",
                "required": ["name", "description", "price", "category_id"],
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome do produto"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição do produto"
                    },
                    "price": {
                        "type": "number",
                        "format": "float",
                        "description": "Preço do produto"
                    },
                    "category_id": {
                        "type": "integer",
                        "description": "ID da categoria do produto"
                    }
                }
            },
            "ProductPatchInput": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome do produto"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição do produto"
                    },
                    "price": {
                        "type": "number",
                        "format": "float",
                        "description": "Preço do produto"
                    },
                    "category_id": {
                        "type": "integer",
                        "description": "ID da categoria do produto"
                    }
                }
            },
            "Error": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Mensagem de erro"
                    }
                }
            }
        }
    }
}

def setup_swagger(app):
    """Configura o Swagger UI para a aplicação Flask"""
    
    # Define uma rota para servir o arquivo swagger.json
    @app.route('/api/swagger.json')
    def swagger_json():
        return jsonify(SWAGGER_DEFINITION)
    
    # Cria o blueprint do Swagger UI
    swagger_ui = get_swaggerui_blueprint(
        base_url='/api/docs',
        api_url='/api/swagger.json',
        config={
            'app_name': "SSK Products API",
            'layout': 'BaseLayout',
            'deepLinking': True,
        }
    )
    
    # Registra o blueprint do Swagger UI
    app.register_blueprint(swagger_ui, url_prefix='/api/docs')
    
    return app
