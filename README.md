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

## Análise Estática de Código

O projeto utiliza várias ferramentas de análise estática para garantir a qualidade do código:

### Ferramentas Configuradas

- **Ruff**: Linter e formatter rápido para Python
- **mypy**: Verificador de tipagem estática
- **Bandit**: Ferramenta de análise de segurança
- **Pylint**: Linter completo com regras específicas para Flask

### Pre-commit Hooks

O projeto utiliza pre-commit hooks para verificar o código antes de cada commit:

```bash
# Instalação
pip install -r requirements-dev.txt
pre-commit install

# Executar manualmente em todos os arquivos
pre-commit run --all-files
```

### Execução Manual das Ferramentas

Você pode executar todas as ferramentas de análise estática manualmente:

```bash
./run_linters.sh
```

Ou individualmente:

```bash
# Ruff (linter)
python -m ruff check src/

# Ruff (formatter)
python -m ruff format src/

# mypy (verificação de tipos)
python -m mypy src/

# Bandit (análise de segurança)
python -m bandit -r src/ -c pyproject.toml

# Pylint
python -m pylint src/
```

### Correção Automática de Erros de Linting

Para corrigir automaticamente muitos problemas de linting, você pode usar o script `docker_fix.sh`:

```bash
# No host:
chmod +x docker_fix.sh
docker cp docker_fix.sh api:/application/
docker exec -it api bash

# Dentro do contêiner:
chmod +x docker_fix.sh
./docker_fix.sh
```

Este script irá:
1. Aplicar correções automáticas com Ruff
2. Formatar o código com Ruff
3. Corrigir problemas de nova linha no final dos arquivos
4. Corrigir comparações com None
5. Substituir prints por loggers
6. Corrigir variáveis não utilizadas
7. Tentar corrigir linhas longas
8. Configurar o Ruff para ignorar erros específicos que não podem ser facilmente corrigidos

### Verificação Regular de Qualidade de Código

Para realizar verificações regulares de qualidade de código, você pode:

1. **Usar o script de verificação de qualidade**:
```bash
./run_code_quality.sh
```

2. **Configurar execução automática**:
```bash
# Instalar como hook de pre-push do Git
cp run_code_quality_check.sh .git/hooks/pre-push
chmod +x .git/hooks/pre-push

# Ou agendar execução regular com cron
# Exemplo: Verificar a qualidade do código todo dia útil às 9h
# 0 9 * * 1-5 cd /caminho/do/projeto && ./run_code_quality_check.sh >> /tmp/quality_check.log 2>&1
```

### Integração com CI/CD

O projeto está configurado com GitHub Actions para executar verificações de código automaticamente:
- Em cada push para as branches `main`, `master`, `develop` e `DEV-*`
- Em cada pull request para as branches `main`, `master` e `develop`

O arquivo de configuração está em `.github/workflows/code-analysis.yml`.

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