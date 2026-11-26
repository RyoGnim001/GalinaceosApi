
# Estagio 1: instala as dependencias
FROM python:3.12-slim AS builder

WORKDIR /build

# Instala o uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copia os arquivos de gerenciamento de dependencias
COPY pyproject.toml uv.lock ./

# Instala as dependencias do projeto
RUN uv sync --frozen --no-dev --no-install-project

# Estagio 2: imagem final
FROM python:3.12-slim AS production

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Copia o ambiente virtual criado no builder
COPY --from=builder /build/.venv /app/.venv

# Copia os arquivos da API
COPY . .

EXPOSE 5001

CMD ["python", "main.py"]
