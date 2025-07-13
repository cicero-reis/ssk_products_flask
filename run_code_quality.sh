#!/bin/bash
set -e

echo "============================================="
echo "Executando verificações de qualidade de código"
echo "============================================="

echo -e "\n1. Verificando formatação e erros de linting com Ruff..."
python -m ruff check src/ || true

echo -e "\n2. Verificando erros de tipagem com mypy..."
python -m mypy src/ || true

echo -e "\n3. Verificando vulnerabilidades de segurança com Bandit..."
python -m bandit -r src/ -c pyproject.toml || true

echo -e "\n4. Verificando problemas com Pylint..."
python -m pylint src/ || true

echo -e "\n============================================="
echo "Verificações completas! Verifique os resultados acima."
echo "============================================="
