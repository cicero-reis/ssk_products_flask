# Use a imagem oficial mais recente do Python como base
FROM python:3.9-alpine

LABEL maintainer="Cicero Reis"

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho no container
WORKDIR /application

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Atualize o pip e instale pacotes necessários
RUN apk update && \
    apk add --no-cache bash gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir gunicorn

# Copia o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev libffi-dev openssl-dev

# Copia o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta em que a aplicação é executada
EXPOSE 5000

# Crie um usuário não-root e defina as permissões corretas
RUN adduser -D user && \
    chown -R user:user /application && \
    chmod -R 775 /application

USER user

# Execute a aplicação usando Gunicorn
# CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]

# Execute a aplicação
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
