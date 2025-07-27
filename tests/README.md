# Testes Unitários

Este diretório contém testes unitários para o projeto SSK Products Flask, que testam componentes isoladamente sem dependências de banco de dados ou outros serviços externos.

## Estrutura

```
tests/
├── conftest.py              # Configurações globais para os testes
├── utils/                   # Utilitários para testes
│   ├── app_context.py       # Helpers para criar contexto de aplicação Flask
│   └── stubs.py             # Classes stub para substituir componentes reais
└── unit/                    # Testes unitários
    └── application/         # Testes para a camada de aplicação
        ├── category/        # Testes para o módulo de categorias
        │   ├── commands/    # Testes para comandos de categoria
        │   ├── dtos/        # Testes para DTOs de categoria
        │   ├── events/      # Testes para eventos de categoria
        │   └── queries/     # Testes para consultas de categoria
        └── product/         # Testes para o módulo de produtos
            ├── commands/    # Testes para comandos de produto
            ├── dtos/        # Testes para DTOs de produto
            ├── events/      # Testes para eventos de produto
            └── queries/     # Testes para consultas de produto
```

## Como executar

Para executar os testes unitários:

```bash
./run_tests.sh
```

Este script irá executar todos os testes unitários e gerar um relatório de cobertura.

## Abordagem de Testes

### Mocking

Utilizamos `unittest.mock` para criar mocks das dependências, como repositórios e publishers de eventos.

### Stubs

Para classes que dependem de recursos externos, como o contexto da aplicação Flask (`current_app`), 
criamos stubs que substituem essas dependências por implementações simplificadas para testes.

### Fixtures

Utilizamos fixtures do pytest para configurar o ambiente de teste e reutilizar código comum.

### Padrão AAA

Os testes seguem o padrão Arrange-Act-Assert (AAA):

1. **Arrange**: Configura o cenário de teste
2. **Act**: Executa o código que está sendo testado
3. **Assert**: Verifica se o resultado é o esperado
