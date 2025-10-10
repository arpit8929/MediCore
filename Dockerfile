# Use Python 3.9 slim image for optimal size and compatibility
FROM python:3.9-slim

# Set environment variables for Python optimization
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_ENV=production \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for ML packages
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libc6-dev \
    libffi-dev \
    libssl-dev \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Upgrade pip and install wheel for better package building
RUN pip install --upgrade pip setuptools wheel

# Copy requirements first for better Docker layer caching
COPY requirements.txt /app/

# Install Python dependencies with specific versions
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Create necessary directories for the application
RUN mkdir -p /app/website/uploads \
    /app/website/static/images \
    /app/website/static/css \
    /app/website/static/js \
    /app/website/static/fonts \
    /app/instance

# Set proper permissions for web server access
RUN chmod -R 755 /app/website/static \
    && chmod -R 755 /app/website/uploads \
    && chmod -R 755 /app/website/templates

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Health check to ensure the application is running
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Run the application with gunicorn optimized for ML workloads
CMD ["gunicorn", \
     "--bind", "0.0.0.0:5000", \
     "--workers", "2", \
     "--worker-class", "sync", \
     "--worker-connections", "1000", \
     "--timeout", "300", \
     "--keep-alive", "2", \
     "--max-requests", "1000", \
     "--max-requests-jitter", "100", \
     "--preload", \
     "app:app"]
