# Base leve do sistema, já com Python 3.11
FROM python:3.11-slim

# Pasta central de operações dentro do container
WORKDIR /app

# Mostra os logs/prints imediatamente (sem guardar em buffer)
ENV PYTHONUNBUFFERED=1

# Injeta o código local dentro do container
COPY src/ /app/src/

# Comando que dispara a execução da aplicação
CMD ["python", "src/main.py"]
