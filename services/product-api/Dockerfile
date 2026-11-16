FROM python:3.13-slim

WORKDIR /app

# Apply available Debian security updates
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# Copy production dependencies
COPY requirements.txt .

# Upgrade packaging tools and install production dependencies
RUN python -m pip install --no-cache-dir --upgrade \
      pip "setuptools>=78.1.1" \
    && python -m pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY app/ ./app/

# Run as a non-root user
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]