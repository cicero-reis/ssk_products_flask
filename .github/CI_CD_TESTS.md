# Testes no Pipeline CI/CD

Este documento descreve como os testes são executados no pipeline de CI/CD.

## Configuração no GitHub Actions

Os testes unitários são executados automaticamente como parte do pipeline de CI/CD no GitHub Actions. Isso garante que cada commit ou pull request seja verificado quanto à qualidade do código e funcionalidade antes de ser integrado ao branch principal.

## O que é testado?

O pipeline de CI/CD executa:

1. **Testes unitários** - Testam componentes individuais isoladamente
2. **Relatório de cobertura** - Geram métricas de cobertura de código

## Como os testes são executados

```yaml
- name: Run unit tests
  run: |
    echo "🧪 Executando testes unitários..."
    pytest tests/unit -v --cov=application --cov=domain --cov-report=term --cov-report=xml
```

## Relatório de cobertura

O relatório de cobertura é gerado em formato XML e enviado para o Codecov (ou outra ferramenta de análise de cobertura) para visualização e análise.

```yaml
- name: Upload coverage report
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage.xml
    fail_ci_if_error: false
```

## Dependências

As dependências necessárias para a execução dos testes são instaladas automaticamente no pipeline:

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r docker/requirements.txt
    pip install -r requirements-test.txt
```

## Execução local

Para executar os testes localmente da mesma forma que o CI/CD, utilize o script `run_tests.sh`:

```bash
./run_tests.sh
```

Este script executa os testes unitários e gera um relatório de cobertura em HTML para visualização local.
