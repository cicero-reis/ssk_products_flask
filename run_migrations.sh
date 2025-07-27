#!/bin/bash

# Script para rodar as migrations do projeto Flask/SQLAlchemy usando Alembic

export FLASK_APP=app.py

# Ativar venv se existir
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Rodar as migrations
alembic upgrade head
