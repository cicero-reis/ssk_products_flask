#!/bin/bash
set -e

# 🎨 Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m' # Sem cor

PYTHON=$(which python)
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
LOG_DIR="logs"
LOG_FILE="$LOG_DIR/verificacao_$TIMESTAMP.log"

mkdir -p "$LOG_DIR"

echo -e "${BLUE}🐍 Usando Python: $PYTHON${NC}" | tee -a "$LOG_FILE"
echo -e "${BLUE}🔍=============================================${NC}" | tee -a "$LOG_FILE"
echo -e "${BLUE}🔍 Executando verificações de qualidade de código${NC}" | tee -a "$LOG_FILE"
echo -e "${BLUE}🔍=============================================${NC}" | tee -a "$LOG_FILE"

# Verifica se as ferramentas estão instaladas
check_tool() {
    if ! $PYTHON -m "$1" --version &>/dev/null; then
        echo -e "${RED}❌ Ferramenta '$1' não encontrada. Instale com: pip install $1${NC}" | tee -a "$LOG_FILE"
        exit 1
    fi
}

for tool in ruff mypy bandit pylint; do
    check_tool $tool
done

echo -e "\n${YELLOW}🧹 1. Verificando formatação e linting com Ruff...${NC}" | tee -a "$LOG_FILE"
echo "   ✏️  1.1. Corrigindo problemas automaticamente..." | tee -a "$LOG_FILE"
$PYTHON -m ruff check --fix src/ 2>&1 | tee -a "$LOG_FILE" || echo -e "${YELLOW}⚠️  Problemas corrigidos automaticamente.${NC}" | tee -a "$LOG_FILE"

echo "   🔍 1.2. Verificando problemas restantes..." | tee -a "$LOG_FILE"
$PYTHON -m ruff check src/ 2>&1 | tee -a "$LOG_FILE" || echo -e "${YELLOW}⚠️  Ainda existem problemas de linting.${NC}" | tee -a "$LOG_FILE"

echo -e "\n${YELLOW}📐 2. Verificando erros de tipagem com mypy...${NC}" | tee -a "$LOG_FILE"
$PYTHON -m mypy src/ 2>&1 | tee -a "$LOG_FILE" || echo -e "${YELLOW}⚠️  Verifique os erros de tipagem acima.${NC}" | tee -a "$LOG_FILE"

echo -e "\n${YELLOW}🔒 3. Verificando vulnerabilidades com Bandit...${NC}" | tee -a "$LOG_FILE"
$PYTHON -m bandit -r src/ 2>&1 | tee -a "$LOG_FILE" || echo -e "${YELLOW}⚠️  Vulnerabilidades encontradas.${NC}" | tee -a "$LOG_FILE"

echo -e "\n${YELLOW}🧠 4. Verificando boas práticas com Pylint...${NC}" | tee -a "$LOG_FILE"
$PYTHON -m pylint src/ 2>&1 | tee -a "$LOG_FILE" || echo -e "${YELLOW}⚠️  Pylint encontrou sugestões ou problemas.${NC}" | tee -a "$LOG_FILE"

echo -e "\n${GREEN}✅=============================================${NC}" | tee -a "$LOG_FILE"
echo -e "${GREEN}✅ Verificações completas! Veja os resultados acima.${NC}" | tee -a "$LOG_FILE"
echo -e "${GREEN}✅ Log salvo em: $LOG_FILE${NC}" | tee -a "$LOG_FILE"
