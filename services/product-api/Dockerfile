
# Stage 1: Build production dependencies
FROM python:3.13-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN python -m pip install --no-cache-dir \
    --prefix=/install \
    -r requirements.txt

# Stage 2: Production runtime
FROM python:3.13-slim

# Remove packaging tools unnecessary at runtime
RUN python -m pip uninstall -y pip setuptools wheel

WORKDIR /app

# Apply available Debian security updates
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# Copy installed application dependencies
COPY --from=builder /install /usr/local

# Copy application source
COPY app/ ./app/

# Create non-root user
RUN useradd --create-home appuser

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
