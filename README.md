# SSK PRODUCTS FLASK

## Sobre o Projeto

Aplicação Flask para gerenciamento de produtos e categorias.

## Estrutura do Projeto

O projeto segue uma arquitetura limpa, com separação clara entre as camadas:

- **application**: Contém a lógica de aplicação (commands, queries, dtos, events)
- **domain**: Contém as entidades e interfaces de repositórios
- **infra**: Contém implementações de infraestrutura (banco de dados, serviços externos)
- **presentation**: Contém os controllers e schemas para API
- **tests**: Contém os testes unitários e de integração

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