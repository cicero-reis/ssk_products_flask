from flask import jsonify
from flask_swagger_ui import get_swaggerui_blueprint

# Definição da especificação OpenAPI como um dicionário
SWAGGER_DEFINITION = {
    "openapi": "3.0.0",
    "info": {
        "title": "SSK Products API",
        "description": "API para gerenciamento de produtos e categorias com suporte a upload de imagens",
        "version": "1.0.0",
        "contact": {
            "name": "Equipe de Desenvolvimento",
            "email": "dev@example.com"
        }
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
                        "description": "ID único da categoria",
                        "example": 1
                    },
                    "name": {
                        "type": "string",
                        "description": "Nome da categoria",
                        "example": "Eletrônicos"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição da categoria",
                        "example": "Produtos eletrônicos como smartphones, tablets e acessórios"
                    }
                }
            },
            "CategoryInput": {
                "type": "object",
                "required": ["name", "description"],
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome da categoria",
                        "example": "Eletrodomésticos"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição da categoria",
                        "example": "Produtos para cozinha, lavanderia e outros eletrodomésticos"
                    }
                }
            },
            "CategoryPatchInput": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome da categoria (opcional)",
                        "example": "Eletrônicos - Atualizado"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição da categoria (opcional)",
                        "example": "Descrição atualizada da categoria de eletrônicos"
                    }
                }
            },
            "Product": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID único do produto",
                        "example": 1
                    },
                    "name": {
                        "type": "string",
                        "description": "Nome do produto",
                        "example": "Smartphone XYZ"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição do produto",
                        "example": "Smartphone com câmera de alta resolução, 128GB de armazenamento"
                    },
                    "price": {
                        "type": "number",
                        "format": "float",
                        "description": "Preço do produto",
                        "example": 1299.99
                    },
                    "category_id": {
                        "type": "integer",
                        "description": "ID da categoria do produto",
                        "example": 1
                    },
                    "original_name": {
                        "type": "string",
                        "description": "Nome original da imagem do produto",
                        "example": "smartphone_xyz.jpg"
                    },
                    "stored_filename": {
                        "type": "string",
                        "description": "URL da imagem do produto no S3",
                        "example": "https://s3.amazonaws.com/bucket-name/products/abc123.jpg"
                    }
                }
            },
            "ProductInput": {
                "type": "object",
                "required": ["name", "description", "price", "category_id"],
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome do produto",
                        "example": "Tablet ABC"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição do produto",
                        "example": "Tablet com tela de 10 polegadas, 64GB de armazenamento"
                    },
                    "price": {
                        "type": "number",
                        "format": "float",
                        "description": "Preço do produto",
                        "example": 899.90
                    },
                    "category_id": {
                        "type": "integer",
                        "description": "ID da categoria do produto",
                        "example": 1
                    }
                }
            },
            "ProductPatchInput": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome do produto (opcional)",
                        "example": "Tablet ABC Pro"
                    },
                    "description": {
                        "type": "string",
                        "description": "Descrição do produto (opcional)",
                        "example": "Tablet atualizado com tela de 10 polegadas, 128GB de armazenamento"
                    },
                    "price": {
                        "type": "number",
                        "format": "float",
                        "description": "Preço do produto (opcional)",
                        "example": 999.90
                    },
                    "category_id": {
                        "type": "integer",
                        "description": "ID da categoria do produto (opcional)",
                        "example": 2
                    }
                }
            },
            "Error": {
                "type": "object",
                "properties": {
                    "error": {
                        "type": "string",
                        "description": "Mensagem de erro",
                        "example": "Recurso não encontrado"
                    },
                    "code": {
                        "type": "integer",
                        "description": "Código de erro HTTP (opcional)",
                        "example": 404
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
            'displayRequestDuration': True,
            'defaultModelsExpandDepth': 3,
            'defaultModelExpandDepth': 3,
            'docExpansion': 'list',  # 'list', 'full', or 'none'
            'supportedSubmitMethods': ['get', 'post', 'put', 'delete', 'patch'],
            'operationsSorter': 'alpha',  # 'alpha' para ordenar alfabeticamente
        }
    )
    
    # Registra o blueprint do Swagger UI
    app.register_blueprint(swagger_ui, url_prefix='/api/docs')
    
    app.logger.info('Swagger UI configurado em /api/docs')
    app.logger.info('Documentação OpenAPI disponível em /api/swagger.json')
    
    return app
