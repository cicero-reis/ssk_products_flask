# SSK PRODUCTS FLASK

## Sobre o Projeto

Aplicação Flask para gerenciamento de produtos e categorias.

## Estrutura do Projeto

O projeto segue uma arquitetura limpa, com separação clara entre as camadas:

- **src/**
  - **application**: Contém a lógica de aplicação (commands, queries, dtos, events)
  - **domain**: Contém as entidades e interfaces de repositórios
  - **infra**: Contém implementações de infraestrutura (banco de dados, serviços externos)
  - **presentation**: Contém os controllers e schemas para API
  - **ioc**: Contém a configuração de injeção de dependências
  - **errors**: Contém manipuladores de erro personalizados
  - **utils**: Contém funções utilitárias
- **tests**: Contém os testes unitários e de integração
- **terraform**: Contém arquivos de infraestrutura como código
- **docker**: Contém configurações para containerização

## API Documentation (Swagger/OpenAPI)

A documentação da API está disponível via Swagger UI. Após iniciar a aplicação, acesse:

```
http://localhost:5000/api/docs
```

A especificação OpenAPI em formato JSON está disponível em:

```
http://localhost:5000/api/swagger.json
```

### Recursos da Documentação Swagger

A documentação inclui:
- Todos os endpoints disponíveis, organizados por tags (Categorias e Produtos)
- Métodos HTTP suportados para cada endpoint (GET, POST, PUT, DELETE, PATCH)
- Parâmetros de requisição e formatos esperados
- Exemplos de payload para requisições
- Esquemas de resposta com exemplos
- Códigos de status e possíveis erros

### Usando o Swagger UI

1. Navegue para `http://localhost:5000/api/docs`
2. Explore os endpoints disponíveis expandindo as seções
3. Teste os endpoints diretamente na interface:
   - Clique em um endpoint para expandir
   - Clique em "Try it out"
   - Preencha os parâmetros necessários
   - Clique em "Execute"
   - Veja a resposta da API, incluindo status code e corpo da resposta

## Testes

### Testes Unitários

Os testes unitários estão localizados em `tests/unit/` e podem ser executados com o seguinte comando:

```bash
./run_tests.sh
```

Este script irá executar todos os testes unitários e gerar um relatório de cobertura em `htmlcov/index.html`.

### Configuração para Testes

Para configurar o ambiente de teste, execute:

```bash
./setup_tests.sh
```

### CI/CD

Os testes são executados automaticamente como parte do pipeline de CI/CD. Para mais informações, consulte [CI_CD_TESTS.md](.github/CI_CD_TESTS.md).

## Docker

O projeto pode ser executado em um container Docker:

```bash
cd docker
docker-compose up
```

## Terraform

Recursos de infraestrutura são gerenciados com Terraform. Os arquivos de configuração estão localizados em `terraform/`.

## Injeção de Dependências

O projeto utiliza o padrão IoC (Inversão de Controle) com a biblioteca `dependency-injector` para gerenciar as dependências. A configuração do container de IoC está localizada em `ioc/container.py`.