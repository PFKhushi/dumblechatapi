FROM python:3.11-slim

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /DumbChat

# Copiar e instalar requirements primeiro (para melhor cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Criar diretório para logs se necessário
RUN mkdir -p /DumbChat/logs

# Expor a porta
EXPOSE 5000

# Comando padrão (será sobrescrito pelo Render)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "DumbChat:DumbChat"]