#!/bin/bash
# Script para executar testes unitários

# Define cores para o output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Iniciando execução dos testes unitários...${NC}"

# Executa os testes com coverage
python -m pytest tests/unit -v --cov=application --cov=domain --cov-report=term --cov-report=html

# Verifica se os testes passaram
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Todos os testes passaram!${NC}"
else
    echo -e "${RED}Alguns testes falharam. Verifique os erros acima.${NC}"
fi

echo -e "${YELLOW}Relatório de cobertura gerado em: htmlcov/index.html${NC}"
