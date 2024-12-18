# Biblioteca oficial do Python
FROM python:3.9-slim

# Instalação das dependências
RUN apt-get update && apt-get install -y \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Definição de variáveis de ambiente para o Chrome
ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver

# Diretório para trabalho no container
WORKDIR /app

# Trazendo arquivos para o ambiente do container
COPY requirements.txt /app/
COPY *.py /app/

# Instalação das bibliotecas do arquivo requirements
RUN pip install --no-cache-dir -r requirements.txt

# Criação da pasta de extração
RUN mkdir -p /app/extract/logs

# Comando para rodar o script
CMD ["python", "main.py"]
