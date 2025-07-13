#!/bin/bash
set -e

# Verifica se o Python está disponível e mostra o caminho
if command -v python &>/dev/null; then
    echo "Usando Python: $(which python)"
else
    echo "AVISO: Python não encontrado no PATH. Tentando usar o caminho absoluto."
fi

echo "============================================="
echo "Executando verificações de qualidade de código"
echo "============================================="

echo -e "\n1. Verificando formatação e erros de linting com Ruff..."
/usr/local/bin/python -m ruff check src/ || true

echo -e "\n2. Verificando erros de tipagem com mypy..."
/usr/local/bin/python -m mypy src/ || true

echo -e "\n3. Verificando vulnerabilidades de segurança com Bandit..."
/usr/local/bin/python -m bandit -r src/ || true

echo -e "\n4. Verificando problemas com Pylint..."
/usr/local/bin/python -m pylint src/ || true

echo -e "\n============================================="
echo "Verificações completas! Verifique os resultados acima."
echo "============================================="
