FROM python:3.10-slim AS builder

WORKDIR /app

RUN pip install flask

COPY app/ .

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]
