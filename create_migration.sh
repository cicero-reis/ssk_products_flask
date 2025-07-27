#!/bin/bash


# Script para criar uma nova migration Alembic
# OBS: A entidade/tabela 'order' NÃO é mais migrada pelo Alembic/MySQL. Agora é persistida apenas no MongoDB.

if [ -z "$1" ]; then
  echo "Uso: $0 <mensagem-da-migration>"
  exit 1
fi

export FLASK_APP=app.py

# Ativar venv se existir
if [ -d "venv" ]; then
    source venv/bin/activate
fi

alembic revision --autogenerate -m "$1"
