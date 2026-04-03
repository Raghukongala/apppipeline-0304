FROM python:3.10-slim as builder

WORKDIR /app
COPY app/ /app
RUN pip install flask

FROM python:3.10-slim

WORKDIR /app
COPY --from=builder /app /app

EXPOSE 5000

CMD ["python", "app.py"]
