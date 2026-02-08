FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory in the container
WORKDIR /app

# Copy project dependencies files
COPY pyproject.toml poetry.lock* uv.lock* ./

# Install the application dependencies.
RUN uv sync --frozen --no-cache

# Copy the application code
COPY . .

# Create a non-root user
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port 8000 (common port for FastAPI applications)
EXPOSE 8000

# Run the application using uvicorn instead of fastapi CLI for production
CMD ["sh", "-c", "/app/.venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000"]