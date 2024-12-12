# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Instale as dependências necessárias
RUN apt-get update && apt-get install -y \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Defina variáveis de ambiente para o Chrome
ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver

# Crie um diretório de trabalho
WORKDIR /app

# Copie os arquivos do script e o requirements.txt para o diretório de trabalho
COPY requirements.txt /app/
COPY web_scraper.py /app/

# Instale as bibliotecas Python necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o script
CMD ["python", "web_scraper.py"]
