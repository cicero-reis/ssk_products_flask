#!/bin/bash
# Script para instalar dependências de teste

echo "Instalando dependências de teste..."
pip install -r docker/requirements.txt
pip install -r requirements-test.txt

echo "Dependências instaladas com sucesso!"
