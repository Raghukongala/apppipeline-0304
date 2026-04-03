# -------- Build Stage --------
FROM python:3.10-slim AS builder

WORKDIR /app

# Copy dependency file first for caching
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# -------- Runtime Stage --------
FROM python:3.10-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy app
COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]
