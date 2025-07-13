#!/bin/bash
# Script para instalar dependências de teste

echo "Instalando dependências de teste..."
pip3 install -r docker/requirements.txt
pip3 install -r requirements-test.txt

echo "Dependências instaladas com sucesso!"
